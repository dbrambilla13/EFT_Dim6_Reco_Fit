# run with python make_ll_plots_2d.py config_two_ops.py operators_two_ops.py

import os
import sys

# my modules
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

# change dir to output dir
os.chdir(cf.tag)

# create output csv file (and REMOVE the older one)
f = open("results.csv","w")
# write first line
f.write("operator,variable,1sigmaL,1sigmaR,2sigmaL,2sigmaR\n")
f.close()

# create output dir for likelihood scans
if (os.path.isdir("ll_scans") == False):
    os.mkdir("ll_scans")

# loop on all operators and variables

for couple in ops.op_couple :
    for var in ops.op_couple[couple]['variables'] :   
        op1 = ops.op_couple[couple]['op1']
        op2 = ops.op_couple[couple]['op2']
        
        print ( "\n>>> processing {}_{} : {}".format(op1,op2,var))

        os.system("root higgsCombineTest.MultiDimFit.mH125_{}_{}_{}.root \
        ../draw2D.cxx\(\\\"{}\",\\\"{}\\\",\\\"k_{}\\\",\\\"k_c{}\\\"\)".format(op1,op2,var,op1,op2,op1,op2))

        # rename ll file and move to folder
        os.system("mv ll_scan_2D.png ll_scans/{}_{}_{}_ll_scan.png\n".format(op1,op2,var)) 
     
# come back to script dir
os.chdir(script_dir)












