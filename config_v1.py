tag='test_moduli'
# tag = 'dim2_distrib'

# various parameters
combine_folder="/afs/cern.ch/user/d/dbrambil/combine/CMSSW_10_2_13/src/"
# main config
sr_config_path="/afs/cern.ch/user/d/dbrambil/CMSSW_10_2_18/src/PlotsConfigurations/Configurations/VBS/EFT/Full2018_multiEftOps/"
# control region config
wz_config_path="/afs/cern.ch/user/d/dbrambil/CMSSW_10_2_18/src/PlotsConfigurations/Configurations/VBS/EFT/Full2018_cr_WZ/"

# datacard folder signal region 
dc_folder_sr="/datacards_VBS_SS_2018_multiEFT_may11/"
# dc_folder_sr="/datacards_VBS_SS_2018_multiEFT_may09_less_nuisances/"
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

# for condor submission
queue_name = "microcentury"