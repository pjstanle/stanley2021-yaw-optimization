# Copyright 2021 NREL

# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

# See https://floris.readthedocs.io for documentation

import numpy as np
import matplotlib.pyplot as plt

import floris.tools as wfct

import time
import pyoptsparse

import inspect



def calc_aep(yaw_array):

    global floris_model
    global yaw_scale
    global wd
    global ws
    global wf
    global nturbs

    ndirs = len(wd)    
    aep = 0.0
    
    for i in range(ndirs):
        aep += wfct.floris_interface.global_calc_one_AEP_case(floris_model, wd[i], ws[i], wf[i], yaw=yaw_array[i*nturbs:(i+1)*nturbs])
    
    return aep


def obj_func_full(input_dict):

    # calculate the wind farm AEP as a function of the grid design variables
    global function_calls
    global aep_scale
    global yaw_scale

    yaw_array = input_dict["yaw_array"]*yaw_scale

    funcs = {}
    fail = False

    # objective
    aep = calc_aep(yaw_array)
    function_calls += 1
    funcs["aep_obj"] = -aep/aep_scale

    return funcs, fail


def obj_func_one(input_dict):

    # calculate the wind farm AEP as a function of the grid design variables
    global function_calls
    global aep_scale
    global yaw_scale
    global yaw_array
    global turbine_index

    iter_yaw = np.copy(yaw_array)
    iter_yaw[turbine_index] = input_dict["turbine_yaw"]

    funcs = {}
    fail = False

    # objective
    aep = calc_aep(iter_yaw)
    function_calls += 1
    funcs["aep_obj"] = -aep/aep_scale

    return funcs, fail


def place_turbines(nturbs,side,rotor_diameter,min_spacing):
    turbine_x = np.array([])
    turbine_y = np.array([])
    for i in range(nturbs):
        placed = False
        while placed == False:
            temp_x = np.random.rand()*side
            temp_y = np.random.rand()*side
            good_point = True
            for j in range(len(turbine_x)):
                dist = np.sqrt((temp_y - turbine_y[j])**2 + (temp_x - turbine_x[j])**2)
                if dist < min_spacing:
                    good_point = False
            if good_point == True:
                turbine_x = np.append(turbine_x,temp_x)
                turbine_y = np.append(turbine_y,temp_y)
                placed = True

    return turbine_x, turbine_y


if __name__=="__main__":

    global floris_model
    global wd
    global ws
    global wf
    global nturbs

    global yaw_scale
    global aep_scale


    floris_model = wfct.floris_interface.FlorisInterface("/Users/astanley/Data/turbines/15mw_240d_150h.json")
    floris_model.set_gch(True)

    nturbs_array = [10,20,30,40,50,60,70,80,90,100]
    spacing_array = [3,4,5,6,7,8]

    for m in range(len(nturbs_array)):
        for n in range(len(spacing_array)):
            nturbs = nturbs_array[m]
            spacing = spacing_array[n]
            progress_filename = "line_layout/continuous/continuous_%sspacing"%spacing
    
            wd = np.array([270.0])
            ws = np.array([10.0])
            wf = np.array([1.0])

            turbine_x = np.linspace(0,240*spacing*(nturbs-1),nturbs)
            turbine_y = np.zeros(nturbs)
        
            start_time = time.time()
            sort_idx = np.argsort(turbine_x)
            turbine_x = turbine_x[sort_idx]
            turbine_y = turbine_y[sort_idx]
            floris_model.reinitialize_flow_field(layout_array=(turbine_x,turbine_y))
            start_aep = calc_aep(np.zeros(nturbs))

            yaw_scale = 0.1
            aep_scale = start_aep
            opt = "SNOPT"
            start_yaw = np.zeros(nturbs)
        
            function_calls = 0
            start_time = time.time()
            optProb = pyoptsparse.Optimization("yaw_optimization",obj_func_full)
            optProb.addVarGroup("yaw_array",nturbs,type="c",lower=0.0,upper=30.0/yaw_scale,value=start_yaw)
            if opt=="SNOPT":
                optimize = pyoptsparse.SNOPT()
            elif opt=="SLSQP":
                optimize = pyoptsparse.SLSQP()
            optProb.addObj("aep_obj")
            solution = optimize(optProb,sens="FD")

            opt_aep = solution.objectives["aep_obj"].value
            opt_yaw = solution.getDVs()["yaw_array"]

            time_gb = time.time()-start_time
            aep_gb = -opt_aep*aep_scale
            yaw_gb = opt_yaw*yaw_scale
            func_gb = function_calls

            file = open('%s.txt'%progress_filename, 'a')
            file.write("nturbs = " + '%s'%nturbs + '\n')
            file.write("percent_increase = " + '%s'%((aep_gb-start_aep)/start_aep*100) + '\n')
            file.write("start_aep = " + '%s'%start_aep + '\n')
            file.write("opt_aep = " + '%s'%aep_gb + '\n')
            file.write("time = " + '%s'%(time.time()-start_time) + '\n')
            file.write("funcs = " + '%s'%function_calls + '\n' +'\n')
            file.close()

            file = open('%s_yaw.txt'%progress_filename, 'a')
            file.write("nturbs = " + '%s'%nturbs + '\n')
            file.write("yaw_angles = np." + '%s'%repr(yaw_gb) + '\n' + '\n')
            file.close()

