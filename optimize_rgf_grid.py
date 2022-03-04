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

from new_optimizer import GF1


def calc_aep(yaw_array):

    global floris_model
    global wd
    global ws
    global wf
    global nturbs

    ndirs = len(wd)    
    aep = 0.0
    
    for i in range(ndirs):
        aep += wfct.floris_interface.global_calc_one_AEP_case(floris_model, wd[i], ws[i], wf[i], yaw=yaw_array[i*nturbs:(i+1)*nturbs])
    
    return aep


def obj_func_full(yaw_array):

    # calculate the wind farm AEP as a function of the grid design variables
    global function_calls

    # objective
    aep = calc_aep(yaw_array)
    function_calls += 1

    return -aep


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
    global function_calls

    function_calls = 0

    floris_model = wfct.floris_interface.FlorisInterface("/Users/astanley/Data/turbines/15mw_240d_150h.json")
    floris_model.set_gch(True)

    n_rows_array = [3,4,5,6,7,8,9,10]
    direction_array = [0,15,30,45,60,75]

    for m in range(len(n_rows_array)):
        for n in range(len(direction_array)):

            function_calls = 0
            wind_direction = direction_array[n]
            nrows = n_rows_array[m]
            progress_filename = "grid_layout/continuous/continuous_%sdir"%(wind_direction)
    
            wd = np.array([270.0])
            ws = np.array([10.0])
            wf = np.array([1.0])

            x_row = np.linspace(0,240*5*(nrows-1),nrows)
            y_row = np.linspace(0,240*5*(nrows-1),nrows) 
            temp_x, temp_y = np.meshgrid(x_row,y_row)
            temp_x = np.ndarray.flatten(temp_x)
            temp_y = np.ndarray.flatten(temp_y)

            center = (240*5*(nrows-1))/2.0
            turbine_x = temp_x*np.cos(np.deg2rad(wind_direction)) - temp_y*np.sin(np.deg2rad(wind_direction))
            turbine_y = temp_x*np.sin(np.deg2rad(wind_direction)) + temp_y*np.cos(np.deg2rad(wind_direction))

            nturbs = len(turbine_x)

            start_time = time.time()
            sort_idx = np.argsort(turbine_x)
            turbine_x = turbine_x[sort_idx]
            turbine_y = turbine_y[sort_idx]
            floris_model.reinitialize_flow_field(layout_array=(turbine_x,turbine_y))
            start_aep = calc_aep(np.zeros(nturbs))

            opt = GF1()
             # inputs
            opt.objective_function =  obj_func_full
            opt.bounds = np.zeros((nturbs,2))
            for i in range(nturbs):
                opt.bounds[i] = (0,30)
            opt.n_leaders = 20
            opt.n_followers = 5
            opt.new_leaders = 5
            opt.replace_leaders = 2
            opt.start_radius = 0.2
            opt.alpha = 0.5    
            opt.convergence_iters = 10
        
            opt.optimize()
            solution = opt.solution

            print("wind direction: ", wind_direction)
            print("nrows: ", nrows)
            print("solution: ", solution)
            print("optimal yaw angles: ", opt.optimal_dvs)
            print("function calls: ", function_calls)

            # # opt_aep = solution.objectives["aep_obj"].value
            # # opt_yaw = solution.getDVs()["yaw_array"]

            # time_gb = time.time()-start_time
            # aep_gb = -opt_aep*aep_scale
            # yaw_gb = opt_yaw*yaw_scale
            # func_gb = function_calls

            # file = open('%s.txt'%progress_filename, 'a')
            # file.write("nrows = " + '%s'%nrows + '\n')
            # file.write("percent_increase = " + '%s'%((aep_gb-start_aep)/start_aep*100) + '\n')
            # file.write("start_aep = " + '%s'%start_aep + '\n')
            # file.write("opt_aep = " + '%s'%aep_gb + '\n')
            # file.write("time = " + '%s'%(time.time()-start_time) + '\n')
            # file.write("funcs = " + '%s'%function_calls + '\n' +'\n')
            # file.close()

            # file = open('%s_yaw.txt'%progress_filename, 'a')
            # file.write("nrows = " + '%s'%nrows + '\n')
            # file.write("yaw_angles = np." + '%s'%repr(yaw_gb) + '\n')
            # file.close()

