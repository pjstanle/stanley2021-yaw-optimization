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

if __name__=="__main__":

    global floris_model
    global wd
    global ws
    global wf
    global nturbs

    floris_model = wfct.floris_interface.FlorisInterface("/Users/astanley/Data/turbines/15mw_240d_150h.json")
    floris_model.set_gch(True)

    nturbs = 5
    turbine_x = np.linspace(0,240*5*(nturbs-1),nturbs)
    turbine_y = np.zeros(nturbs)
    floris_model.reinitialize_flow_field(layout_array=(turbine_x,turbine_y))

    wd = 270.0
    ws = 10.0
    floris_model.reinitialize_flow_field(wind_direction=wd,wind_speed=ws)

    yaw_array = np.zeros(nturbs)

    N = 100
    yaw_angle = np.linspace(0.0,30.0,N)
    powers = np.zeros((nturbs,N))
    for i in range(N):
        yaw_array[0] = yaw_angle[i]
        floris_model.calculate_wake(yaw_angles=yaw_array)
        P = floris_model.get_turbine_power()
        for k in range(nturbs):
            powers[k,i] = P[k]

    for k in range(nturbs):
        plt.plot(yaw_angle,powers[k,:],label="%s"%k)
    
    plt.legend()
    plt.show()

    


