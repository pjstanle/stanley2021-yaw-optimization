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
from pandas.core import base
import pyoptsparse

import inspect



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

    locations = np.loadtxt('layout_amalia.txt')
    tx = locations[:, 0]
    ty = locations[:, 1]
    nturbs = len(tx)

    floris_model = wfct.floris_interface.FlorisInterface("/Users/astanley/Data/turbines/2mw_80d_60h.json")
    floris_model.set_gch(True)
    floris_model.reinitialize_flow_field(wind_direction=270.0)

    wd = np.array([0.000000000000000000e+00,5.000000000000000000e+00,1.000000000000000000e+01,1.500000000000000000e+01,
                    2.000000000000000000e+01,2.500000000000000000e+01,3.000000000000000000e+01,3.500000000000000000e+01,
                    4.000000000000000000e+01,4.500000000000000000e+01,5.000000000000000000e+01,5.500000000000000000e+01,
                    6.000000000000000000e+01,6.500000000000000000e+01,7.000000000000000000e+01,7.500000000000000000e+01,
                    8.000000000000000000e+01,8.500000000000000000e+01,9.000000000000000000e+01,9.500000000000000000e+01,
                    1.000000000000000000e+02,1.050000000000000000e+02,1.100000000000000000e+02,1.150000000000000000e+02,
                    1.200000000000000000e+02,1.250000000000000000e+02,1.300000000000000000e+02,1.350000000000000000e+02,
                    1.400000000000000000e+02,1.450000000000000000e+02,1.500000000000000000e+02,1.550000000000000000e+02,
                    1.600000000000000000e+02,1.650000000000000000e+02,1.700000000000000000e+02,1.750000000000000000e+02,
                    1.800000000000000000e+02,1.850000000000000000e+02,1.900000000000000000e+02,1.950000000000000000e+02,
                    2.000000000000000000e+02,2.050000000000000000e+02,2.100000000000000000e+02,2.150000000000000000e+02,
                    2.200000000000000000e+02,2.250000000000000000e+02,2.300000000000000000e+02,2.350000000000000000e+02,
                    2.400000000000000000e+02,2.450000000000000000e+02,2.500000000000000000e+02,2.550000000000000000e+02,
                    2.600000000000000000e+02,2.650000000000000000e+02,2.700000000000000000e+02,2.750000000000000000e+02,
                    2.800000000000000000e+02,2.850000000000000000e+02,2.900000000000000000e+02,2.950000000000000000e+02,
                    3.000000000000000000e+02,3.050000000000000000e+02,3.100000000000000000e+02,3.150000000000000000e+02,
                    3.200000000000000000e+02,3.250000000000000000e+02,3.300000000000000000e+02,3.350000000000000000e+02,
                    3.400000000000000000e+02,3.450000000000000000e+02,3.500000000000000000e+02,3.550000000000000000e+02])

    ws = np.array([7.443989372765817514e+00,7.037473467697797247e+00,7.098204875283014026e+00,6.975827202579733211e+00,
                    7.099063879774560881e+00,6.793840398569997774e+00,6.613868624428271836e+00,6.887240030040243433e+00,
                    7.280119386040773577e+00,7.361887161929981716e+00,8.711165432347877768e+00,8.487120544890457197e+00,
                    8.292666171934786945e+00,8.201185831179456542e+00,8.373684353408945569e+00,7.581321273563128571e+00,
                    7.220830604679464138e+00,6.843751211396981837e+00,6.971049344118904756e+00,7.002524339758943839e+00,
                    6.413119393145527702e+00,5.275072132632170785e+00,5.768902039588225783e+00,0.000000000000000000e+00,
                    0.000000000000000000e+00,0.000000000000000000e+00,6.599693305235294183e+00,6.616581240762715588e+00,
                    6.647338295302516187e+00,7.472358052240274162e+00,8.618059180445825973e+00,8.759846978365571246e+00,
                    9.677066728256948025e+00,9.323521917193836828e+00,9.216675349128450989e+00,8.719007778913285378e+00,
                    8.817304334084926865e+00,8.887524347760965782e+00,9.492215428301701508e+00,9.934646503111826732e+00,
                    1.084229158881114330e+01,1.106679327602730112e+01,1.061125577114793828e+01,1.092747238717757163e+01,
                    1.128913549145671169e+01,1.060262813772340884e+01,1.045290065497462351e+01,9.735850631582730230e+00,
                    9.058025175439807342e+00,8.783981653725767558e+00,8.593467905562416576e+00,8.736410238545547102e+00,
                    8.251111368880540198e+00,7.924095405453314811e+00,7.742623908089139917e+00,7.888630724347134304e+00,
                    7.862056793378839892e+00,7.909226766898133754e+00,8.624877191489668249e+00,8.410354617807987765e+00,
                    8.220820932359574229e+00,8.321741539102298191e+00,8.430233322798232010e+00,8.580956434400002664e+00,
                    8.848850793045777152e+00,8.190563105779933295e+00,8.266538227899193458e+00,8.581777873969919312e+00,
                    8.058018314533699211e+00,7.791763321868974579e+00,7.414568224050260170e+00,7.830039408380693011e+00])

    wf = np.array([1.178129090726009499e-02,1.099587151344275440e-02,9.606283355150539369e-03,1.212365320712919213e-02,
                    1.047225858423119459e-02,1.006947940791461105e-02,9.686839190413855730e-03,1.000906253146712291e-02,
                    1.037156379015205000e-02,1.121740006041687700e-02,1.522505286476689111e-02,1.562783204108347465e-02,
                    1.574866579397845093e-02,1.705769811700735133e-02,1.935353942201188324e-02,1.419796596515960144e-02,
                    1.206323633068170399e-02,1.202295841305004581e-02,1.321115698318396994e-02,1.746047729332393661e-02,
                    1.729936562279730042e-02,1.439935555331789407e-02,7.874332896989225464e-03,0.000000000000000000e+00,
                    2.013895881582922239e-05,0.000000000000000000e+00,3.423622998690967569e-04,3.564595710401772394e-03,
                    7.189608297251032058e-03,8.800725002517370554e-03,1.135837277212768150e-02,1.415768804752794326e-02,
                    1.669519685832242598e-02,1.631255664082166892e-02,1.317087906555231176e-02,1.091531567817943804e-02,
                    9.485449602255563092e-03,1.010975732554626923e-02,1.188198570133924131e-02,1.260698821870909203e-02,
                    1.588963850568925543e-02,1.770214479911388569e-02,2.042090423925083109e-02,2.279730137951867935e-02,
                    2.954385258282146709e-02,3.028899405900714950e-02,2.698620481321115788e-02,2.215285469741214500e-02,
                    2.124660155069982986e-02,1.828617460477293191e-02,1.661464102305910615e-02,1.901117712214278610e-02,
                    1.905145503977444255e-02,1.639311247608498529e-02,1.762158896385056933e-02,1.653408518779578978e-02,
                    1.445977242976538048e-02,1.403685429463296698e-02,1.657436310542744970e-02,1.562783204108347465e-02,
                    1.534588661766186739e-02,1.752089416977142128e-02,1.597019434095257179e-02,1.510421911187191657e-02,
                    1.452018930621286862e-02,1.345282448897392076e-02,1.478199577081864939e-02,1.339240761252643262e-02,
                    1.105628838989024254e-02,1.045211962541536636e-02,1.162017923673346054e-02,1.105628838989024254e-02])

    
    # floris_model.reinitialize_flow_field(wind_speed=ws[index])

    yaw_angle = 20.0
    start_time = time.time()
    function_calls = 0

    baseline_aep = 0.0
    optimized_aep = 0.0

    baseline_power_array = np.zeros(len(wd))
    optimized_power_array = np.zeros(len(wd))
    percent_improvement_array = np.zeros(len(wd))

    for n in range(len(wd)):

        print(n)
        
        wind_direction = wd[n] - 270.0
        turbine_x = tx*np.cos(np.deg2rad(wind_direction)) - ty*np.sin(np.deg2rad(wind_direction))
        turbine_y = tx*np.sin(np.deg2rad(wind_direction)) + ty*np.cos(np.deg2rad(wind_direction))
        sort_idx = np.argsort(turbine_x)
        turbine_x = turbine_x[sort_idx]
        turbine_y = turbine_y[sort_idx]
        floris_model.reinitialize_flow_field(layout_array=(turbine_x,turbine_y))
        floris_model.reinitialize_flow_field(wind_speed=ws[n])

        waking = check_waking(turbine_x,turbine_y,80.0)
        best_power = 0.0
        yaw_array = np.zeros(nturbs)
        temp_yaw = np.zeros(nturbs)
        
        for i in range(nturbs):
            if waking[i] == True:
                temp_yaw[:] = yaw_array[:]
                temp_yaw[i] = yaw_angle
                floris_model.calculate_wake(yaw_angles=(temp_yaw))
                temp_power = floris_model.get_farm_power()
                function_calls += 1
                if temp_power > best_power:
                    yaw_array[i] = temp_yaw[i]
                    best_power = temp_power
        
        optimized_aep += best_power*8760.0*wf[n]
        floris_model.calculate_wake(yaw_angles=(np.zeros(nturbs)))
        base_power = floris_model.get_farm_power()
        baseline_aep += base_power*8760.0*wf[n]

        baseline_power_array[n] = base_power
        optimized_power_array[n] = best_power
        percent_improvement_array[n] = (best_power-base_power)/base_power*100.0


    print("percent_increase = " + '%s'%((optimized_aep-baseline_aep)/baseline_aep*100))
    print("baseline_aep = " + '%s'%baseline_aep)
    print("optimized_aep = " + '%s'%optimized_aep)
    print("time = " + '%s'%(time.time()-start_time))
    print("funcs = " + '%s'%function_calls)

    print("baseline_power_array = np." + '%s'%repr(baseline_power_array))
    print("optimized_power_array = np." + '%s'%repr(optimized_power_array))
    print("percent_improvement_array = np." + '%s'%repr(percent_improvement_array))


    progress_filename = "amalia_discrete"
    file = open('%s.txt'%progress_filename, 'a')
    file.write("percent_increase = " + '%s'%((optimized_aep-baseline_aep)/baseline_aep*100) + '\n')
    file.write("baseline_aep = " + '%s'%baseline_aep + '\n')
    file.write("optimized_aep = " + '%s'%optimized_aep + '\n')
    file.write("time = " + '%s'%(time.time()-start_time) + '\n')
    file.write("funcs = " + '%s'%function_calls + '\n' +'\n')

    file.write("baseline_power_array = np." + '%s'%repr(baseline_power_array) + '\n' +'\n')
    file.write("optimized_power_array = np." + '%s'%repr(optimized_power_array) + '\n' +'\n')
    file.write("percent_improvement_array = np." + '%s'%repr(percent_improvement_array) + '\n' +'\n')
    file.close()