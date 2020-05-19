tag = 'def_2op'

# various parameters
combine_folder="/afs/cern.ch/user/d/dbrambil/combine/CMSSW_10_2_13/src/"
# main config
sr_config_path="/afs/cern.ch/user/d/dbrambil/CMSSW_10_2_18/src/PlotsConfigurations/Configurations/VBS/EFT/Full2018_EFT_TwoOps/"
# control region config
wz_config_path="/afs/cern.ch/user/d/dbrambil/CMSSW_10_2_18/src/PlotsConfigurations/Configurations/VBS/EFT/Full2018_cr_WZ/"

# datacard folder signal region 
dc_folder_sr="/datacards_VBS_SS_2018_EFT_TwoOps_may16/"
# dc_folder_sr="/datacards_VBS_SS_2018_multiEFT_may09_less_nuisances/"
# datacard folder WZ control region 
dc_folder_wz="/datacards_VBS_SS_2018_cr_WZ_full_nuis_mar03/"
# regions
sr_cut="SS_sr_emu"
wz_cut="wz_vbs_total"

# combine AnalyticAnomalousCoupling model  
AAC_model = "HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFT:analiticAnomalousCouplingEFT"

# combine likelihood scan options (should be set for each operator instead...)
n_points="14400"  # for grid 120*120=14400
# n_points="1000"  # TEST VALUE
verbosity=0

# for condor submission
queue_name = "workday"

# full dim6 operators list
operator_list = ['k_cG','k_cGtil','k_cH','k_cHB','k_cHBtil','k_cHDD','k_cHG','k_cHGtil','k_cHW','k_cHWB','k_cHWBtil','k_cHWtil','k_cHbox','k_cHd','k_cHe','k_cHl1','k_cHl3','k_cHq1','k_cHq3','k_cHu','k_cHudAbs','k_cHudPh','k_cW','k_cWtil','k_cdBAbs','k_cdBPh','k_cdGAbs','k_cdGPh','k_cdHAbs','k_cdHPh','k_cdWAbs','k_cdWPh','k_cdd','k_cdd1','k_ceBAbs','k_ceBPh','k_ceHAbs','k_ceHPh','k_ceWAbs','k_ceWPh','k_ced','k_cee','k_ceu','k_cld','k_cle','k_cledqAbs','k_cledqPh','k_clequ1Abs','k_clequ1Ph','k_clequ3Abs','k_clequ3Ph','k_cll','k_cll1','k_clq1','k_clq3','k_clu','k_cqd1','k_cqd8','k_cqe','k_cqq1','k_cqq11','k_cqq3','k_cqq31','k_cqu1','k_cqu8','k_cquqd1Abs','k_cquqd1Ph','k_cquqd8Abs','k_cquqd8Ph','k_cuBAbs','k_cuBPh','k_cuGAbs','k_cuGPh','k_cuHAbs','k_cuHPh','k_cuWAbs','k_cuWPh','k_cud1','k_cud8','k_cuu','k_cuu1']

