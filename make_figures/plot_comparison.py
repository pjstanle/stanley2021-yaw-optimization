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


# random layouts
nseeds = 7
ind = 10

percent_discrete = np.zeros(ind)
time_discrete = np.zeros(ind)
funcs_discrete = np.zeros(ind)
percent_continuous = np.zeros(ind)
time_continuous = np.zeros(ind)
funcs_continuous = np.zeros(ind)

for k in range(nseeds):
    random_seed = k
    nturbs,percent_increase,start_aep,opt_aep,time,funcs = read_layout_file("/Users/astanley/Projects/delayed_projects/stanley2021-yaw-optimization/random_layout/discrete/discrete_seed%s_20yaw.txt"%random_seed)
    nturbs_c,percent_increase_c,start_aep_c,opt_aep_c,time_c,funcs_c = read_layout_file("/Users/astanley/Projects/delayed_projects/stanley2021-yaw-optimization/random_layout/continuous/continuous_seed%s_.txt"%random_seed)
    percent_discrete += percent_increase
    time_discrete += time
    funcs_discrete += funcs
    
    percent_continuous += percent_increase_c
    time_continuous += time_c
    funcs_continuous += funcs_c

pd = percent_discrete/nseeds
td = time_discrete/nseeds
fd = funcs_discrete/nseeds

pc = percent_continuous/nseeds
tc = time_continuous/nseeds
fc = funcs_continuous/nseeds

plt.figure(figsize=(5,5))
ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)

ax1.plot(nturbs[0:ind],pd[0:ind],"o")
ax1.plot(nturbs_c[0:ind],pc[0:ind],"o")
ax1.set_ylim(0,5)
# ax1.plot(nturbs[0:ind],percent_increase_c[0:ind]/percent_increase[0:ind],"o")

# ax2.plot(nturbs[0:ind],td[0:ind],"o")
# ax2.plot(nturbs_c[0:ind],tc[0:ind],"o")
ax2.plot(nturbs[0:ind],tc[0:ind]/td[0:ind],"o")
ax2.

# ax3.plot(nturbs[0:ind],fd[0:ind],"o",label="discrete")
# ax3.plot(nturbs_c[0:ind],fc[0:ind],"o",label="continuous")
ax3.plot(nturbs[0:ind],fc[0:ind]/fd[0:ind],"o")
# ax3.legend(loc=2)

# ax3.plot(nturbs[0:ind],funcs_c[0:ind]/funcs[0:ind],"o")
# ax3.set_ylim(0,100)

plt.show()




# grid layouts



# for k in range(nseeds):
#     random_seed = k
#     nturbs,percent_increase,start_aep,opt_aep,time,funcs = read_layout_file("discrete/discrete_seed%s.txt"%random_seed)
#     nturbs_c,percent_increase_c,start_aep_c,opt_aep_c,time_c,funcs_c = read_layout_file("continuous/continuous_seed%s_.txt"%random_seed)

#     pd += percent_increase
#     td += time
#     fd += funcs
    
#     pc += percent_increase_c
#     tc += time_c
#     fc += funcs_c

# percent_increase = pd/nseeds
# time = td/nseeds
# funcs = fd/nseeds

# percent_increase_c = pc/nseeds
# time_c = tc/nseeds
# funcs_c = fc/nseeds

# plt.figure(figsize=(5,5))
# ax1 = plt.subplot(311)
# ax2 = plt.subplot(312)
# ax3 = plt.subplot(313)


# ax1.plot(nturbs[0:ind],percent_increase[0:ind],"o")
# ax1.plot(nturbs_c[0:ind],percent_increase_c[0:ind],"o")
# # ax1.plot(nturbs[0:ind],percent_increase_c[0:ind]/percent_increase[0:ind],"o")

# ax2.plot(nturbs[0:ind],time[0:ind],"o")
# ax2.plot(nturbs_c[0:ind],time_c[0:ind],"o")
# # ax2.plot(nturbs[0:ind],time_c[0:ind]/time[0:ind],"o")

# ax3.plot(nturbs[0:ind],funcs[0:ind],"o",label="discrete")
# ax3.plot(nturbs_c[0:ind],funcs_c[0:ind],"o",label="continuous")
# # ax3.legend(loc=2)

# # ax3.plot(nturbs[0:ind],funcs_c[0:ind]/funcs[0:ind],"o")
# # ax3.set_ylim(0,100)



# plt.show()
