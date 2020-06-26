# this is just a first try
# use the more complete scripts sub_all.py and sub_all_2Ops.py


# first setup combine ... ()
# cd ~/combine/CMSSW_10_2_13/src/ ; cmsenv ; cd -

import os

# my modules
import config as cf
import operators as ops

# define output dir for everything
if (os.path.isdir(cf.tag) == False):
    os.mkdir(cf.tag)
script_dir=os.getcwd()
os.chdir(cf.tag)


# create output csv file (and REMOVE the older one)
f = open("results.csv","w")
# write first line
f.write("operator,variable,1sigmaL,1sigmaR,2sigmaL,2sigmaR\n")
f.close()

# define output dir for likelihood scans
if (os.path.isdir("ll_scans") == False):
    os.mkdir("ll_scans")
    
# define operators, variables and ranges!


# now the true code begins!

for op in ops.operator :
    for var in ops.operator[op]['variables'] :
        print('>>> processing {}:{}'.format(op,var)) 
        print('range: ({},{})'.format(ops.operator[op]['range'][0],ops.operator[op]['range'][1]))
        
        # combine datacards
        datacard1= "{}/{}/{}/events/datacard.txt".format(cf.wz_config_path,cf.dc_folder_wz,cf.wz_cut)
        datacard2= "{}/{}/{}/{}/datacard.txt".format(cf.sr_config_path,cf.dc_folder_sr,cf.sr_cut,var)
        combined_datacard= "combined_dc_{}_{}_{}.txt".format(cf.sr_cut,cf.wz_cut,var)
        os.system("combineCards.py {} {} > {}".format(datacard1,datacard2,combined_datacard))

        # create workspace from combined datacard
        model_file= "combined_dc_{}_{}_{}_model_test.root".format(cf.sr_cut,cf.wz_cut,var)
        os.system("text2workspace.py {} -P {} -o {} ".format(combined_datacard, cf.AAC_model,model_file))
    
        # do likelihood scan with combine
        os.system("combine -M MultiDimFit {} --algo=grid --points {} -m 125 \
            -t -1 --expectSignal=1 --redefineSignalPOIs k_{} \
            --freezeParameters r,k_cG,k_cGtil,k_cH,k_cHB,k_cHBtil,k_cHDD,k_cHG,k_cHGtil,k_cHW,k_cHWB,k_cHWBtil,k_cHWtil,k_cHbox,k_cHd,k_cHe,k_cHl1,k_cHl3,k_cHq1,k_cHq3,k_cHu,k_cHudAbs,k_cHudPh,k_cW,k_cWtil,k_cdBAbs,k_cdBPh,k_cdGAbs,k_cdGPh,k_cdHAbs,k_cdHPh,k_cdWAbs,k_cdWPh,k_cdd,k_cdd1,k_ceBAbs,k_ceBPh,k_ceHAbs,k_ceHPh,k_ceWAbs,k_ceWPh,k_ced,k_cee,k_ceu,k_cld,k_cle,k_cledqAbs,k_cledqPh,k_clequ1Abs,k_clequ1Ph,k_clequ3Abs,k_clequ3Ph,k_cll,k_cll1,k_clq1,k_clq3,k_clu,k_cqd1,k_cqd8,k_cqe,k_cqq1,k_cqq11,k_cqq3,k_cqq31,k_cqu1,k_cqu8,k_cquqd1Abs,k_cquqd1Ph,k_cquqd8Abs,k_cquqd8Ph,k_cuBAbs,k_cuBPh,k_cuGAbs,k_cuGPh,k_cuHAbs,k_cuHPh,k_cuWAbs,k_cuWPh,k_cud1,k_cud8,k_cuu,k_cuu1 --setParameters r=1\
            --setParameterRanges k_{}={},{} \
            --verbose {}    ".format   (model_file, # model file
                                        cf.n_points, # number of points for the grid
                                        op, op, # operators (two times...)
                                        ops.operator[op]['range'][0], # range l for op
                                        ops.operator[op]['range'][1], # range r for op
                                        cf.verbosity)) # verbosity option

        # plot likelihood scan and find intersections
        os.system("root -l -b higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.MultiDimFit.mH125.root  \
            ../draw_v1.cxx\(\\\"k_{}\\\",\\\"{}\\\"\) -q".format(op,var))
        
        # rename ll file and move to folder
        os.system("mv ll.png ll_scans/{}_{}_ll_scan.png ".format(op,var)) 

# tidy up files...
if (os.path.isdir("datacards_and_models") == False):
    os.mkdir("datacards_and_models")
os.system("mv combined*.txt datacards_and_models")
os.system("mv combined*.root datacards_and_models")

# come back to script dir
os.chdir(script_dir)
