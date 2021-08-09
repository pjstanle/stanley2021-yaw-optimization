from logging import error
import matplotlib.pyplot as plt
import numpy as np
import csv

from numpy.core.einsumfunc import _einsum_path_dispatcher


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



spacing = [3,4,5,6,7,8]
pd = np.zeros((len(spacing),5))
pc = np.zeros((len(spacing),5))

td = np.zeros((len(spacing),5))
tc = np.zeros((len(spacing),5))

ad = np.zeros((len(spacing),5))
ac = np.zeros((len(spacing),5))


for i in range(len(spacing)):
    nturbs,percent_discrete,start_aep,opt_discrete,time_discrete,funcs_discrete = read_layout_file("/Users/astanley/Projects/active_projects/stanley2021-yaw-optimization/line_layout/discrete/discrete_%sspacing_20yaw.txt"%spacing[i])
    nturbs_c,percent_continuous,start_aep_c,opt_continuous,time_continuous,funcs_continuous = read_layout_file("/Users/astanley/Projects/active_projects/stanley2021-yaw-optimization/line_layout/continuous/continuous_%sspacing.txt"%spacing[i])

    pd[i,:] = percent_discrete[:]
    pc[i,:] = percent_continuous[:]
    td[i,:] = time_discrete[:]
    tc[i,:] = time_continuous[:]
    ad[i,:] = opt_discrete[:]
    ac[i,:] = opt_continuous[:]


plt.figure(figsize=(6,4))
ax1 = plt.subplot(221)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
ax2 = plt.subplot(222)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
ax3 = plt.subplot(223)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
ax4 = plt.subplot(224)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)

ax1.plot(spacing,pc[:,4],"o",label="continuous")
ax1.plot(spacing,pd[:,4],"o",label="Boolean")
ax1.set_ylim(0,330)
ax1.set_ylabel("% power increase\nfrom baseline",fontsize=8)
ax1.legend(fontsize=8)

ax2.plot(spacing,ac[:,4]/ad[:,4],"o",color="C3")
ax2.set_ylabel("opt power continuous/\nopt power Boolean",fontsize=8)

ax3.plot(spacing,tc[:,4],"o")
ax3.plot(spacing,td[:,4],"o")
ax3.set_ylabel("time to run\noptimization (s)",fontsize=8)
ax3.set_ylim(-50,1100)
ax3.set_xlabel("turbine spacing (D)",fontsize=8)
# ax3.set_ylabel("time continuous/\ntime boolean)",fontsize=8)

ax4.plot(spacing,tc[:,4]/td[:,4],"o",color="C3")
# ax4.set_ylim(0,70)
ax4.set_ylabel("time continuous/\ntime Boolean",fontsize=8)
ax4.set_xlabel("turbine spacing (D)",fontsize=8)

plt.suptitle(r"50 turbines in-line: $\bf{varied}$ $\bf{turbine}$ $\bf{spacing}$",fontsize=8)
plt.subplots_adjust(top=0.93,left=0.13,right=0.99,bottom=0.1,
            wspace=0.5,hspace=0.2)

ax1.set_xticks((3,4,5,6,7,8))
ax2.set_xticks((3,4,5,6,7,8))
ax3.set_xticks((3,4,5,6,7,8))
ax4.set_xticks((3,4,5,6,7,8))

plt.savefig("figures/line_results_spacing.pdf",transparent=True)

plt.show()



