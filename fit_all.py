import os

tag='v2'

# define output dir for everything
if (os.path.isdir(tag) == False):
    os.mkdir(tag)

# various parameters
combine_folder="/afs/cern.ch/user/d/dbrambil/combine/CMSSW_10_2_13/src/"
# main config
sr_config_path="/afs/cern.ch/user/d/dbrambil/CMSSW_10_2_18/src/PlotsConfigurations/Configurations/VBS/EFT/Full2018_multiEftOps/"
# control region config
wz_config_path="/afs/cern.ch/user/d/dbrambil/CMSSW_10_2_18/src/PlotsConfigurations/Configurations/VBS/EFT/Full2018_cr_WZ/"

# datacard folder signal region
dc_folder_sr="/datacards_VBS_SS_2018_multiEFT_may07/" 
# datacard folder WZ control region 
dc_folder_wz="/datacards_VBS_SS_2018_cr_WZ_full_nuis_mar03/"
# regions
sr_cut="SS_sr_emu"
wz_cut="wz_vbs_total"

# combine AnalyticAnomalousCoupling model  
AAC_model = "HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFT:analiticAnomalousCouplingEFT"

# combine likelihood scan options (should be set for each operator instead...)
n_points="120"
verbosity=0

# setup combine environment
save_dir=os.getcwd()
os.chdir(combine_folder)
os.system('eval `scramv1 runtime -sh`')
os.chdir(save_dir)

# create output csv file (and REMOVE the older one)
f = open("results.csv","w")
# write first line
f.write("operator,variable,1sigmaL,1sigmaR,2sigmaL,2sigmaR\n")
f.close()

# define output dir for likelihood scans
if (os.path.isdir("ll_scans") == False):
    os.mkdir("ll_scans")
    
# define operators, variables and ranges!
operator = {}

operator['cHDD'] = {
                    'variables' : ('jetpt1','etaj1','detajj','pt1'),
                    'range' : (-4,4)
}

operator['cHWB'] = {
                    'variables' : ('jetpt1','etaj1','detajj','pt1'),
                    'range' : (-4,4)
}

operator['cHW'] = {
                    'variables' : ('pt1','pt2','mll'),
                    'range' : (-8,8)
}

operator['cHbox'] = {
                    'variables' : ('etaj1','jetpt1','pt2'),
                    'range' : (-1,1)
}

# missing bsm term!
# operator['cHl1'] = {
#                     'variables' : ('pt1','pt2','mll'),
#                     'range' : (-100,100)
# }

# not produced
# operator['cHl3'] = {
#                     'variables' : ('pt1','jetpt1','detajj','etaj1'),
#                     'range' : (-2,2)
# }

# not produced
# operator['cHq1'] = {
#                     'variables' : ('jetpt1','pt1','mll'),
#                     'range' : (-3,3)
# }

operator['cHq3'] = {
                    'variables' : ('pt1','jetpt1','mll','detajj'), # to be invented
                    'range' : (-5,4)
}

operator['cW'] = {
                    'variables' : ('pt1','mll'), # already known
                    'range' : (-1,1)
}

operator['cll1'] = {
                    'variables' : ('pt1','jetpt1','mll','detajj'), # to be invented
                    'range' : (-10,5)
}

# not produced
# operator['cll'] = {
#                     'variables' : ('pt1','mll','dphijj'),
#                     'range' : (-100,100 )
# }

operator['cqq11'] = {
                    'variables' : ('etaj1','dphijj','detajj','jetpt1'),
                    'range' : (-2,2)
}

operator['cqq1'] = {
                    'variables' : ('etaj1','dphijj','detajj','jetpt1'),
                    'range' : (-2,2)
}

operator['cqq31'] = {
                    'variables' : ('etaj1','dphijj','detajj','jetpt1'),
                    'range' : (-0.7,0.7)
}

operator['cqq3'] = {
                    'variables' : ('etaj1','dphijj','detajj','jetpt1'),
                    'range' : (-0.7,0.7)
}



# now the true code begins!

for op in operator :
    for var in operator[op]['variables'] :
        print('>>> processing {}:{}'.format(op,var)) 
        print('range: ({},{})'.format(operator[op]['range'][0],operator[op]['range'][1]))
        
        # combine datacards
        datacard1= "{}/{}/{}/events/datacard.txt".format(wz_config_path,dc_folder_wz,wz_cut)
        datacard2= "{}/{}/{}/{}/datacard.txt".format(sr_config_path,dc_folder_sr,sr_cut,var)
        combined_datacard= "combined_dc_{}_{}_{}.txt".format(sr_cut,wz_cut,var)
        os.system("combineCards.py {} {} > {}".format(datacard1,datacard2,combined_datacard))

        # create workspace from combined datacard
        model_file= "combined_dc_{}_{}_{}_model_test.root".format(sr_cut,wz_cut,var)
        os.system("text2workspace.py {} -P {} -o {} ".format(combined_datacard, AAC_model,model_file))
    
        # do likelihood scan with combine
        os.system("combine -M MultiDimFit {} --algo=grid --points {} -m 125 \
            -t -1 --expectSignal=1 --redefineSignalPOIs k_{} \
            --freezeParameters r,k_cG,k_cGtil,k_cH,k_cHB,k_cHBtil,k_cHDD,k_cHG,k_cHGtil,k_cHW,k_cHWB,k_cHWBtil,k_cHWtil,k_cHbox,k_cHd,k_cHe,k_cHl1,k_cHl3,k_cHq1,k_cHq3,k_cHu,k_cHudAbs,k_cHudPh,k_cW,k_cWtil,k_cdBAbs,k_cdBPh,k_cdGAbs,k_cdGPh,k_cdHAbs,k_cdHPh,k_cdWAbs,k_cdWPh,k_cdd,k_cdd1,k_ceBAbs,k_ceBPh,k_ceHAbs,k_ceHPh,k_ceWAbs,k_ceWPh,k_ced,k_cee,k_ceu,k_cld,k_cle,k_cledqAbs,k_cledqPh,k_clequ1Abs,k_clequ1Ph,k_clequ3Abs,k_clequ3Ph,k_cll,k_cll1,k_clq1,k_clq3,k_clu,k_cqd1,k_cqd8,k_cqe,k_cqq1,k_cqq11,k_cqq3,k_cqq31,k_cqu1,k_cqu8,k_cquqd1Abs,k_cquqd1Ph,k_cquqd8Abs,k_cquqd8Ph,k_cuBAbs,k_cuBPh,k_cuGAbs,k_cuGPh,k_cuHAbs,k_cuHPh,k_cuWAbs,k_cuWPh,k_cud1,k_cud8,k_cuu,k_cuu1 --setParameters r=1\
            --setParameterRanges k_{}={},{} \
            --verbose {}    ".format   (model_file, # model file
                                        n_points, # number of points for the grid
                                        op, op, # operators (two times...)
                                        operator[op]['range'][0], # range l for op
                                        operator[op]['range'][1], # range r for op
                                        verbosity)) # verbosity option

        # plot likelihood scan and find intersections
        os.system("root -l -b higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.MultiDimFit.mH125.root  \
            draw_v1.cxx\(\\\"k_{}\\\",\\\"{}\\\"\) -q".format(op,var))
        
        # rename ll file
        os.system("mv ll.png ll_scans/{}_{}_ll_scan.png ".format(op,var)) 

