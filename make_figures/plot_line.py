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


nturbs,percent_discrete,start_aep,opt_discrete,time_discrete,funcs_discrete = read_layout_file("../line_layout/discrete/discrete_5spacing_20yaw.txt")
nturbs_c,percent_continuous,start_aep_c,opt_continuous,time_continuous,funcs_continuous = read_layout_file("../line_layout/continuous/continuous_5spacing.txt")



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


ax1.plot(nturbs_c,percent_continuous,"o",label="continuous")
ax1.plot(nturbs,percent_discrete,"o",label="Boolean")
ax1.set_ylim(0,105)
ax1.set_ylabel("% power increase\nfrom baseline",fontsize=8)
ax1.legend(fontsize=8)

ax2.plot(nturbs,opt_continuous/opt_discrete,"o",color="C3")
ax2.set_ylabel("opt power continuous/\nopt power Boolean",fontsize=8)

ax3.plot(nturbs_c,time_continuous,"o")
ax3.plot(nturbs,time_discrete,"o")
ax3.set_ylabel("time to run\noptimization (s)",fontsize=8)
ax3.set_xlabel("number of turbines",fontsize=8)
# ax3.set_ylabel("time continuous/\ntime boolean)",fontsize=8)

ax4.plot(nturbs,time_continuous/time_discrete,"o",color="C3")
# ax4.set_ylim(0,70)
ax4.set_ylabel("time continuous/\ntime Boolean",fontsize=8)
ax4.set_xlabel("number of turbines",fontsize=8)

plt.suptitle(r"Turbines in-line: $\bf{varied}$ $\bf{turbine}$ $\bf{number}$",fontsize=8)
plt.subplots_adjust(top=0.93,left=0.13,right=0.99,bottom=0.1,
            wspace=0.5,hspace=0.2)

ax1.set_xticks((10,20,30,40,50))
ax2.set_xticks((10,20,30,40,50))
ax3.set_xticks((10,20,30,40,50))
ax4.set_xticks((10,20,30,40,50))


dy = 0.02
dx = 0.08
limx = ax1.get_xlim()
limy = ax1.get_ylim()
ax1.text(limx[0]+dx*(limx[1]-limx[0]),limy[1]-dy*(limy[1]-limy[0]),"a",fontsize=10,weight="bold")
limx = ax2.get_xlim()
limy = ax2.get_ylim()
ax2.text(limx[0]+dx*(limx[1]-limx[0]),limy[1]-dy*(limy[1]-limy[0]),"b",fontsize=10,weight="bold")
limx = ax3.get_xlim()
limy = ax3.get_ylim()
ax3.text(limx[0]+dx*(limx[1]-limx[0]),limy[1]-dy*(limy[1]-limy[0]),"c",fontsize=10,weight="bold")
limx = ax4.get_xlim()
limy = ax4.get_ylim()
ax4.text(limx[0]+dx*(limx[1]-limx[0]),limy[1]-dy*(limy[1]-limy[0]),"d",fontsize=10,weight="bold")


plt.savefig("figures/line_results.pdf",transparent=True)

plt.show()



