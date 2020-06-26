# EFT_Dim6_Reco_Fit
EFT_Dim6_Reco_Fit

## Procedure

With _sub_all.py_ a job is submitted to Condor to perfor the likelihood scan for each operator and variable defined in _operators.py_.
Then _make_ll_plots.py_ makes plots of the likelihood scans and saves 1 sigma and 2 sigma boundaries in _results.csv_.
A final comparison plot is then produced by _plot_result.py_ using the info in _results.csv_.

Look at _operators.py_ and _config.py_ modules and modify the parameters depending on your needs.

One-dimensional likelihood scans:

    python sub_all.py <config_file>.py <operators_file>.py
    # wait for condor to finish jobs ( chech with condor_queue ) 
    python make_ll_plots.py <config_file>.py <operators_file>.py
    python plot_result.py <config_file>.py <operators_file>.py -b
    
Two-dimensional likelihood scans:

    python sub_all_2Ops config_two_ops.py operators_two_ops.py
    python make_ll_plots_2d.py config_two_ops.py operators_two_ops.py

using combine model from 
https://github.com/amassiro/AnalyticAnomalousCoupling
