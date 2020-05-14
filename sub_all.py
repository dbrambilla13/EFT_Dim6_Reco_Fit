# run with python sub_all.py config_file.py operators_file.py

import os
import sys

# importing modules
config_module_name = str(sys.argv[1])[:-3]
print ("importing module" + config_module_name)
cf = __import__(config_module_name)

operator_module_name = str(sys.argv[2])[:-3]
print ("importing module" + operator_module_name)
ops = __import__(operator_module_name)


# define output dir for everything
if (os.path.isdir(cf.tag) == False):
    os.mkdir(cf.tag)
script_dir=os.getcwd()
os.chdir(cf.tag)


# # create output csv file (and REMOVE the older one)
# f = open("results.csv","w")
# # write first line
# f.write("operator,variable,1sigmaL,1sigmaR,2sigmaL,2sigmaR\n")
# f.close()

# define output dir for likelihood scans
# if (os.path.isdir("ll_scans") == False):
    # os.mkdir("ll_scans")

# now the true code begins!

for op in ops.operator :
    for var in ops.operator[op]['variables'] :
        # open script file
        script_file = open("submit_{}_{}.sh".format(op,var),'w')
        print('>>> creating script for {}:{}'.format(op,var)) 
        print('range: ({},{})'.format(ops.operator[op]['range'][0],ops.operator[op]['range'][1]))
        
        # script first line
        script_file.write("#!/bin/bash\n")

        # combine environment setup
        script_file.write("cd {}\n".format(cf.combine_folder))
        script_file.write("eval `scramv1 runtime -sh` \n")
        script_file.write("cd -\n")

        # combine datacards
        datacard1= "{}/{}/{}/events/datacard.txt".format(cf.wz_config_path,cf.dc_folder_wz,cf.wz_cut)
        datacard2= "{}/{}/{}/{}/datacard.txt".format(cf.sr_config_path,cf.dc_folder_sr,cf.sr_cut,var)
        combined_datacard= "combined_dc_{}_{}_{}.txt".format(cf.sr_cut,cf.wz_cut,var)
        script_file.write("combineCards.py {} {} > {} \n".format(datacard1,datacard2,combined_datacard))

        # create workspace from combined datacard
        model_file= "combined_dc_{}_{}_{}_model_test.root".format(cf.sr_cut,cf.wz_cut,var)
        script_file.write("text2workspace.py {} -P {} -o {} \n".format(combined_datacard, cf.AAC_model,model_file))
    
        # do likelihood scan with combine
        script_file.write("combine -M MultiDimFit {} --algo=grid --points {} -m 125 \
            -t -1 --expectSignal=1 --redefineSignalPOIs k_{} \
            --freezeParameters r,k_cG,k_cGtil,k_cH,k_cHB,k_cHBtil,k_cHDD,k_cHG,k_cHGtil,k_cHW,k_cHWB,k_cHWBtil,k_cHWtil,k_cHbox,k_cHd,k_cHe,k_cHl1,k_cHl3,k_cHq1,k_cHq3,k_cHu,k_cHudAbs,k_cHudPh,k_cW,k_cWtil,k_cdBAbs,k_cdBPh,k_cdGAbs,k_cdGPh,k_cdHAbs,k_cdHPh,k_cdWAbs,k_cdWPh,k_cdd,k_cdd1,k_ceBAbs,k_ceBPh,k_ceHAbs,k_ceHPh,k_ceWAbs,k_ceWPh,k_ced,k_cee,k_ceu,k_cld,k_cle,k_cledqAbs,k_cledqPh,k_clequ1Abs,k_clequ1Ph,k_clequ3Abs,k_clequ3Ph,k_cll,k_cll1,k_clq1,k_clq3,k_clu,k_cqd1,k_cqd8,k_cqe,k_cqq1,k_cqq11,k_cqq3,k_cqq31,k_cqu1,k_cqu8,k_cquqd1Abs,k_cquqd1Ph,k_cquqd8Abs,k_cquqd8Ph,k_cuBAbs,k_cuBPh,k_cuGAbs,k_cuGPh,k_cuHAbs,k_cuHPh,k_cuWAbs,k_cuWPh,k_cud1,k_cud8,k_cuu,k_cuu1 --setParameters r=1\
            --setParameterRanges k_{}={},{} \
            --verbose {}    \n".format   (model_file, # model file
                                        cf.n_points, # number of points for the grid
                                        op, op, # operators (two times...)
                                        ops.operator[op]['range'][0], # range l for op
                                        ops.operator[op]['range'][1], # range r for op
                                        cf.verbosity)) # verbosity option
        script_file.write("mv higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.MultiDimFit.mH125_{}_{}.root \n".format(op,var))
        
        # giving execute permissions
        os.system('chmod 755 submit_{}_{}.sh'.format(op,var))
        
        # creating condor submit file
        condor_file = open("submit_{}_{}.sub".format(op,var),'w')
        condor_file.write("# submit_{}_{}.sub  -- submitting dim6 eft fit\n".format(op,var))
        condor_file.write("executable              = submit_{}_{}.sh\n".format(op,var))
        condor_file.write("log                     = {}_{}.log\n".format(op,var))
        condor_file.write("output                  = {}_{}.out\n".format(op,var))
        condor_file.write("error                   = {}_{}.err\n".format(op,var))
        condor_file.write("queue\n")
        condor_file.write("+JobFlavour = \"{}\"\n".format(cf.queue_name))
        
        condor_file.close()


# submit all jobs to condor
# os.system("for i in *.sub; do condor_submit $i;  done")

# come back to script dir
os.chdir(script_dir)
