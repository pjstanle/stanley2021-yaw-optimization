from logging import error
import matplotlib.pyplot as plt
import numpy as np
import csv


def read_layout_file(filename,TURBS=True):

    nturbs = np.array([])
    nrows = np.array([])
    percent_increase = np.array([])
    start_aep = np.array([])
    opt_aep = np.array([])
    time = np.array([])
    funcs = np.array([])

    with open(filename) as f:
        reader = csv.reader(f)

        x = False
        y = False

        for row in reader:
            if len(row) > 0:
                if TURBS == True:
                    if row[0].split()[0] == "nturbs":
                        nturbs = np.append(nturbs,float(row[0].split()[2]))
                else:
                    if row[0].split()[0] == "nrows":
                        nrows = np.append(nrows,float(row[0].split()[2]))
                if row[0].split()[0] == "percent_increase":
                    percent_increase = np.append(percent_increase,float(row[0].split()[2]))
                if row[0].split()[0] == "start_aep":
                    start_aep = np.append(start_aep,float(row[0].split()[2]))
                if row[0].split()[0] == "opt_aep":
                    opt_aep = np.append(opt_aep,float(row[0].split()[2]))
                if row[0].split()[0] == "time":
                    time = np.append(time,float(row[0].split()[2]))
                if row[0].split()[0] == "funcs":
                    funcs = np.append(funcs,float(row[0].split()[2]))      

    if TURBS == True:
        return nturbs,percent_increase,start_aep,opt_aep,time,funcs
    else: 
        return nrows,percent_increase,start_aep,opt_aep,time,funcs


spacing_arr = [3,4,5,6,7,8]

opt_aep_continuous_line = np.array([])
time_continuous_line = np.array([])
for i in range(len(spacing_arr)):
    filename = "../line_layout/continuous/continuous_%sspacing.txt"%spacing_arr[i]
    nturbs,percent_increase,start_aep,opt_aep,time,funcs = read_layout_file(filename)
    opt_aep_continuous_line = np.append(opt_aep_continuous_line,opt_aep)
    time_continuous_line = np.append(time_continuous_line,time)

opt_aep_discrete_line = np.array([])
time_discrete_line = np.array([])
for i in range(len(spacing_arr)):
    filename = "../line_layout/discrete/discrete_%sspacing_20yaw.txt"%spacing_arr[i]
    nturbs,percent_increase,start_aep,opt_aep,time,funcs = read_layout_file(filename)
    opt_aep_discrete_line = np.append(opt_aep_discrete_line,opt_aep)
    time_discrete_line = np.append(time_discrete_line,time)

aep_ratio_line = opt_aep_continuous_line/opt_aep_discrete_line
time_ratio_line = time_continuous_line/time_discrete_line





opt_aep_continuous_grid = np.array([])
time_continuous_grid = np.array([])
dir_array = [0,15,30,45,60,75]
for i in range(len(dir_array)):
    filename = "../grid_layout/continuous/continuous_%sdir.txt"%dir_array[i]
    nturbs,percent_increase,start_aep,opt_aep,time,funcs = read_layout_file(filename, TURBS=False)
    opt_aep_continuous_grid = np.append(opt_aep_continuous_grid,opt_aep)
    time_continuous_grid = np.append(time_continuous_grid,time)


opt_aep_discrete_grid = np.array([])
time_discrete_grid = np.array([])
dir_array = [0,15,30,45,60,75]
for i in range(len(dir_array)):
    filename = "../grid_layout/discrete/discrete_%sdir_20yaw.txt"%dir_array[i]
    nturbs,percent_increase,start_aep,opt_aep,time,funcs = read_layout_file(filename, TURBS=False)
    opt_aep_discrete_grid = np.append(opt_aep_discrete_grid,opt_aep)
    time_discrete_grid = np.append(time_discrete_grid,time)

aep_ratio_grid = opt_aep_continuous_grid/opt_aep_discrete_grid
time_ratio_grid = time_continuous_grid/time_discrete_grid






seed_arr = [0,1,2,3,4,5,6]

opt_aep_continuous_random = np.array([])
time_continuous_random = np.array([])
for i in range(len(seed_arr)):
    filename = "../random_layout/continuous/continuous_seed%s_.txt"%seed_arr[i]
    nturbs,percent_increase,start_aep,opt_aep,time,funcs = read_layout_file(filename)
    opt_aep_continuous_random = np.append(opt_aep_continuous_random,opt_aep)
    time_continuous_random = np.append(time_continuous_random,time)

opt_aep_discrete_random = np.array([])
time_discrete_random = np.array([])
for i in range(len(seed_arr)):
    filename = "../random_layout/discrete/discrete_seed%s_20yaw.txt"%seed_arr[i]
    nturbs,percent_increase,start_aep,opt_aep,time,funcs = read_layout_file(filename)
    opt_aep_discrete_random = np.append(opt_aep_discrete_random,opt_aep)
    time_discrete_random = np.append(time_discrete_random,time)


aep_ratio_random = opt_aep_continuous_random/opt_aep_discrete_random
time_ratio_random = time_continuous_random/time_discrete_random


aep_ratio_amalia = 336175609805.4604/334240437543.04553
time_ratio_amalia = 67599.27318000793/778.1361200809479



plt.figure(figsize=(4.5,3))
plt.semilogx(time_ratio_line,aep_ratio_line,"o",color="C0",label="line",markersize=5)
plt.semilogx(time_ratio_grid,aep_ratio_grid,"o",color="C1",label="grid",markersize=5)
plt.semilogx(time_ratio_random,aep_ratio_random,"o",color="C3",label="random",markersize=5)
plt.semilogx(time_ratio_amalia,aep_ratio_amalia,"*",color="C2",label="Amalia",markersize=15)

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend(fontsize=8)
plt.xlabel("time ratio",fontsize=8)
plt.ylabel("AEP ratio",fontsize=8)

# plt.gca().set_xticks((10,50,100,200,300,400,500))
# plt.xlim(0,550)
plt.gca().set_xticks((1,10,50,100,200))
plt.gca().set_xticklabels(("1","10","50","100","200"))
plt.grid()
plt.tight_layout()

plt.savefig("aggregate_results.pdf",transparent=True)
plt.show()