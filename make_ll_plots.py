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
for op in ops.operator :
    for var in ops.operator[op]['variables'] :
        
        print ( "\n>>> processing {} : {}".format(op,var))

        os.system("root -l -b higgsCombineTest.MultiDimFit.mH125_{}_{}.root higgsCombineTest.MultiDimFit.mH125_{}_{}.root \
            ../draw_v1.cxx\(\\\"k_{}\\\",\\\"{}\\\"\) -q \n".format(op,var,op,var,op,var))
        
        # rename ll file and move to folder
        os.system("mv ll.png ll_scans/{}_{}_ll_scan.png\n".format(op,var)) 
     
# come back to script dir
os.chdir(script_dir)
