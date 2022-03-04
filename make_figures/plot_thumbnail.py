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
from floris.tools import FlorisInterface
from floris.tools.visualization import visualize_cut_plane, plot_turbines
import pyoptsparse
import time


def objective_function(x):

    global fi
    global start_power
    global scale_x
    global scale_y

    turbine_x = x["turbine_x"]*scale_x
    turbine_y = x["turbine_y"]*scale_y

    fi.reinitialize(layout=[turbine_x,turbine_y])
    fi.calculate_wake()
    farm_power = fi.get_farm_power()
    spacing = calc_spacing(turbine_x, turbine_y)
    fail = False
    funcs = {}
    funcs["obj"] = -np.sum(farm_power)/start_power
    funcs["spacing_con"] = np.min(spacing)

    return funcs, fail


if __name__=="__main__":

    fi = FlorisInterface("gch.yaml")
    nturbines = 4
    D = 126.0
    spacing = 3*D
    turbine_x = np.linspace(0,(nturbines-1)*spacing,nturbines)
    turbine_y = np.zeros(nturbines)

    fi.reinitialize(layout=[turbine_x,turbine_y])

    # plot flow field 
    plt.figure(figsize=(4,4))
    ax1 = plt.subplot(211)
    yaw = np.zeros((1,1,nturbines))
    yaw[0,0,0] = 30.00
    yaw[0,0,1] = 23.71
    yaw[0,0,2] = 16.79
    yaw[0,0,3] = 0.00
    horizontal_plane_2d = fi.calculate_horizontal_plane(yaw_angles=yaw,
                    x_bounds=(np.min(turbine_x)-1.5*D,np.max(turbine_x)+5*D),
                    y_bounds=(-2.5*D,2.5*D),x_resolution=200, y_resolution=100)

    visualize_cut_plane(horizontal_plane_2d, ax=ax1, title="continuous")
    plot_turbines(ax1, turbine_x, turbine_y, yaw[0][0], np.zeros(nturbines)+D, wind_direction=270.0, linewidth=2)
    dy = 20.0
    ax1.text(turbine_x[0],turbine_y[0]+D+dy,r"30.00$^\circ$",fontsize=12,
        horizontalalignment="center",verticalalignment="bottom",weight="bold",
        color="white")
    ax1.text(turbine_x[1],turbine_y[1]+D+dy,r"23.71$^\circ$",fontsize=12,
        horizontalalignment="center",verticalalignment="bottom",weight="bold",
        color="white")
    ax1.text(turbine_x[2],turbine_y[2]+D+dy,r"16.79$^\circ$",fontsize=12,
        horizontalalignment="center",verticalalignment="bottom",weight="bold",
        color="white")
    ax1.text(turbine_x[3],turbine_y[3]+D+dy,r"0.00$^\circ$",fontsize=12,
        horizontalalignment="center",verticalalignment="bottom",weight="bold",
        color="white")
    ax1.axis("off")

    ax2 = plt.subplot(212)
    yaw[0,0,0] = 20
    yaw[0,0,1] = 20
    yaw[0,0,2] = 20
    yaw[0,0,3] = 0

    horizontal_plane_2d = fi.calculate_horizontal_plane(yaw_angles=yaw,
                    x_bounds=(np.min(turbine_x)-1.5*D,np.max(turbine_x)+5*D),
                    y_bounds=(-2.5*D,2.5*D),x_resolution=200, y_resolution=100)
    visualize_cut_plane(horizontal_plane_2d, ax=ax2, title="Boolean")
    plot_turbines(ax2, turbine_x, turbine_y, yaw[0][0], np.zeros(nturbines)+D, wind_direction=270.0, linewidth=2)
    dy = 20.0
    ax2.text(turbine_x[0],turbine_y[0]+D+dy,"TRUE",fontsize=12,
        horizontalalignment="center",verticalalignment="bottom",weight="bold",
        color="white")
    ax2.text(turbine_x[1],turbine_y[1]+D+dy,"TRUE",fontsize=12,
        horizontalalignment="center",verticalalignment="bottom",weight="bold",
        color="white")
    ax2.text(turbine_x[2],turbine_y[2]+D+dy,"TRUE",fontsize=12,
        horizontalalignment="center",verticalalignment="bottom",weight="bold",
        color="white")
    ax2.text(turbine_x[3],turbine_y[3]+D+dy,"FALSE",fontsize=12,
        horizontalalignment="center",verticalalignment="bottom",weight="bold",
        color="black")
    

    ax2.axis("off")

    plt.tight_layout()
    plt.savefig("thumbnail.pdf",transparent=True)
    plt.show()
