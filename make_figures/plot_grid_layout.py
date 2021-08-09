import matplotlib.pyplot as plt
import numpy as np

import floris.tools as wfct

nrows = 5

floris_model = wfct.floris_interface.FlorisInterface("/Users/astanley/Data/turbines/15mw_240d_150h.json")
floris_model.set_gch(True)

x_row = np.linspace(0,240*5*(nrows-1),nrows)
y_row = np.linspace(0,240*5*(nrows-1),nrows) 
temp_x, temp_y = np.meshgrid(x_row,y_row)
turbine_x = np.ndarray.flatten(temp_x)
turbine_y = np.ndarray.flatten(temp_y)
floris_model.reinitialize_flow_field(layout_array=(turbine_x,turbine_y))

dirs = [270,285,300,315,330,345]
plt.figure(figsize=(6,4))

d = 2
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.axis("square")
    plt.axis("off")
    plt.xlim(min(turbine_x)-d*240,max(turbine_x)+d*2*240)
    plt.ylim(min(turbine_y)-d*2*240,max(turbine_y)+d*240)
    floris_model.reinitialize_flow_field(wind_direction=dirs[i],wind_speed=10.0)
    floris_model.calculate_wake()
    hor_plane = floris_model.get_hor_plane(x_resolution=500,y_resolution=500)
    wfct.visualization.visualize_cut_plane(hor_plane, ax=plt.gca())
    plt.title("%s degrees"%int(dirs[i]),fontsize=8)

    for k in range(len(turbine_x)):
        p1 = (turbine_x[k]+120*np.cos(np.deg2rad(dirs[i])),turbine_x[k]-120*np.cos(np.deg2rad(dirs[i])))
        p2 = (turbine_y[k]-120*np.sin(np.deg2rad(dirs[i])),turbine_y[k]+120*np.sin(np.deg2rad(dirs[i])))
        plt.plot(p1,p2,"-k",linewidth=1)

plt.subplots_adjust(top=0.94,bottom=0.01,right=0.99,left=0.01,wspace=0.05)

plt.savefig("grid_layouts.png")
plt.show()