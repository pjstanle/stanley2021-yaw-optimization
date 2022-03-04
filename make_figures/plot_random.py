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

opt_discrete = np.zeros(ind)
opt_continuous = np.zeros(ind)

for k in range(nseeds):
    random_seed = k
    nturbs,percent_increase,start_aep,opt_aep,time,funcs = read_layout_file("../random_layout/discrete/discrete_seed%s_20yaw.txt"%random_seed)
    nturbs_c,percent_increase_c,start_aep_c,opt_aep_c,time_c,funcs_c = read_layout_file("../random_layout/continuous/continuous_seed%s_.txt"%random_seed)
    percent_discrete += percent_increase
    time_discrete += time
    funcs_discrete += funcs
    opt_discrete += opt_aep
    
    percent_continuous += percent_increase_c
    time_continuous += time_c
    funcs_continuous += funcs_c
    opt_continuous += opt_aep_c

pd = percent_discrete/nseeds
td = time_discrete/nseeds
fd = funcs_discrete/nseeds
od = opt_discrete/nseeds

pc = percent_continuous/nseeds
tc = time_continuous/nseeds
fc = funcs_continuous/nseeds
oc = opt_continuous/nseeds

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

ax1.plot(nturbs_c[0:ind],pc[0:ind],"o",label="continuous")
ax1.plot(nturbs[0:ind],pd[0:ind],"o",label="Boolean")
ax1.set_ylim(0,5)
ax1.set_ylabel("% power increase\nfrom baseline",fontsize=8)
ax1.legend(fontsize=8)


ax2.plot(nturbs[0:ind],oc[0:ind]/od[0:ind],"o",color="C3")
ax2.set_ylabel("opt power continuous/\nopt power Boolean",fontsize=8)


ax3.plot(nturbs_c[0:ind],tc[0:ind],"o")
ax3.plot(nturbs[0:ind],td[0:ind],"o")
ax3.set_ylabel("time to run\noptimization (s)",fontsize=8)
ax3.set_xlabel("number of turbines",fontsize=8)
# ax3.set_ylabel("time continuous/\ntime boolean)",fontsize=8)

ax4.plot(nturbs[0:ind],tc[0:ind]/td[0:ind],"o",color="C3")
# ax4.set_ylim(0,180)
ax4.set_ylabel("time continuous/\ntime Boolean",fontsize=8)
ax4.set_xlabel("number of turbines",fontsize=8)


ax1.set_xticks((10,20,30,40,50,60,70,80,90,100))
ax1.set_xticklabels(("","20","","40","","60","","80","","100"))
ax2.set_xticks((10,20,30,40,50,60,70,80,90,100))
ax2.set_xticklabels(("","20","","40","","60","","80","","100"))
ax3.set_xticks((10,20,30,40,50,60,70,80,90,100))
ax3.set_xticklabels(("","20","","40","","60","","80","","100"))
ax4.set_xticks((10,20,30,40,50,60,70,80,90,100))
ax4.set_xticklabels(("","20","","40","","60","","80","","100"))



dy = 0.05
dx = 0.05
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

plt.suptitle(r"Averaged random layout: $\bf{varied}$ $\bf{turbine}$ $\bf{number}$",fontsize=8)
plt.subplots_adjust(top=0.93,left=0.13,right=0.99,bottom=0.1,
            wspace=0.5,hspace=0.2)


plt.savefig("figures/random_results.pdf",transparent=True)

plt.show()



