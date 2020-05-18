# run with python sub_all.py config_file.py operators_file.py

import os
import sys

# importing modules
config_module_name = str(sys.argv[1])[:-3]
print ("importing module " + config_module_name)
cf = __import__(config_module_name)

operator_module_name = str(sys.argv[2])[:-3]
print ("importing module " + operator_module_name)
ops = __import__(operator_module_name)


# define output dir for everything
if (os.path.isdir(cf.tag) == False):
    os.mkdir(cf.tag)
script_dir=os.getcwd()
os.chdir(cf.tag)

op_list = cf.operator_list

for couple in ops.op_couple :
    for var in ops.op_couple[couple]['variables'] :
        # open script file
        op1 = ops.op_couple[couple]['op1']
        op2 = ops.op_couple[couple]['op2']
        range1L = ops.op_couple[couple]['range_op1'][0]
        range1R = ops.op_couple[couple]['range_op1'][1]
        range2L = ops.op_couple[couple]['range_op2'][0]
        range2R = ops.op_couple[couple]['range_op2'][1]

        script_file = open("submit_{}_{}_{}.sh".format(op1,op2,var),'w')
        print('>>> creating script for {}_{}:{}'.format(op1,op2,var)) 
        print('range {}: ({},{})'.format(op1,range1L,range1R))
        print('range {}: ({},{})'.format(op2,range2L,range2R))
        
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
            
        fix_op_list = [x for x in op_list if x != 'k_'+op1 and x != 'k_'+op2]
        sep = ','
        fis_op_string = sep.join(fix_op_list)
        # do likelihood scan with combine
        script_file.write("combine -M MultiDimFit {} --algo=grid --points {} -m 125 \
            -t -1 --expectSignal=1 --redefineSignalPOIs k_{},k_{} \
            --freezeParameters r,{} --setParameters r=1\
            --setParameterRanges k_{}={},{}:k_{}={},{} \
            --verbose {}    \n".format   (model_file, # model file
                                        cf.n_points, # number of points for the grid
                                        op1,op2, # operators 
                                        fis_op_string, # operators to be fixed
                                        op1,range1L, range1R, # range r for op1
                                        op2,range2L, range2R, # range r for op2
                                        cf.verbosity)) # verbosity option
        script_file.write("mv higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.MultiDimFit.mH125_{}_{}_{}.root \n".format(op1,op2,var))
        
        # giving execute permissions
        os.system('chmod 755 submit_{}_{}_{}.sh'.format(op1,op2,var))
        
        # creating condor submit file
        condor_file = open("submit_{}_{}_{}.sub".format(op1,op2,var),'w')
        condor_file.write("# submit_{}_{}_{}.sub  -- submitting dim6 eft fit\n".format(op1,op2,var))
        condor_file.write("executable              = submit_{}_{}_{}.sh\n".format(op1,op2,var))
        condor_file.write("log                     = {}_{}_{}.log\n".format(op1,op2,var))
        condor_file.write("output                  = {}_{}_{}.out\n".format(op1,op2,var))
        condor_file.write("error                   = {}_{}_{}.err\n".format(op1,op2,var))
        condor_file.write("queue\n")
        condor_file.write("+JobFlavour = \"{}\"\n".format(cf.queue_name))
        
        condor_file.close()


# submit all jobs to condor
os.system("for i in *.sub; do condor_submit $i;  done")

# come back to script dir
os.chdir(script_dir)
