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
    global wd
    global ws
    global wf
    global nturbs

    ndirs = len(wd)    
    aep = 0.0
    
    for i in range(ndirs):
        aep += wfct.floris_interface.global_calc_one_AEP_case(floris_model, wd[i], ws[i], wf[i], yaw=yaw_array[i*nturbs:(i+1)*nturbs])
    
    return aep


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


def check_waking(turbine_x,turbine_y,rotor_diameter,spread=0.2):
    sort_idx = np.argsort(turbine_x)
    x = turbine_x[sort_idx]
    y = turbine_y[sort_idx]
    nturbs = len(x)
    waking = np.zeros(nturbs,dtype=bool)
    for i in range(nturbs):
        for j in range(i+1,nturbs):
            r = spread*(x[j]-x[i]) + rotor_diameter/2.0
            if abs(y[j]-y[i]) < (r+rotor_diameter/2.0):
                waking[i] = True
    return waking


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
    
    # nturbs_array = [10,20,30,40,50]
    # yaw_angle_array = [5,10,15,20,25,30]
    # spacing_array = [3,4,5,6,7,8]

    nturbs_array = [10,50]
    yaw_angle_array = [20]
    spacing_array = [5]

    for k in range(len(yaw_angle_array)):
        for m in range(len(nturbs_array)):
            for n in range(len(spacing_array)):
                yaw_angle = yaw_angle_array[k]
                nturbs = nturbs_array[m]
                spacing = spacing_array[n]
                progress_filename = "line_layout/discrete/discrete_%sspacing_%syaw"%(spacing,yaw_angle)
                

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
                waking = check_waking(turbine_x,turbine_y,240.0)
                
                best_aep = start_aep
                yaw_array = np.zeros(nturbs)
                temp_yaw = np.zeros(nturbs)
                function_calls = 0

                for i in range(nturbs):
                    if waking[i] == True:
                        temp_yaw[:] = yaw_array[:]
                        temp_yaw[i] = yaw_angle
                        temp_aep = calc_aep(temp_yaw)
                        function_calls += 1
                        if temp_aep > best_aep:
                            yaw_array[i] = temp_yaw[i]
                            best_aep = temp_aep

                # file = open('%s.txt'%progress_filename, 'a')
                # file.write("nturbs = " + '%s'%nturbs + '\n')
                # file.write("percent_increase = " + '%s'%((best_aep-start_aep)/start_aep*100) + '\n')
                # file.write("start_aep = " + '%s'%start_aep + '\n')
                # file.write("opt_aep = " + '%s'%best_aep + '\n')
                # file.write("time = " + '%s'%(time.time()-start_time) + '\n')
                # file.write("funcs = " + '%s'%function_calls + '\n' +'\n')
                # file.close()

                # file = open('%s_yaw.txt'%progress_filename, 'a')
                # file.write("nturbs = " + '%s'%nturbs + '\n')
                # file.write("yaw_angles = np." + '%s'%repr(yaw_array) + '\n' + '\n')
                # file.close()

        

