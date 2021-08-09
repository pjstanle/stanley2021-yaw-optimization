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
dirs = [0,15,30,45,60,75]
ndirs = len(dirs)
nrows = 8

percent_discrete = np.zeros((ndirs,nrows))
time_discrete = np.zeros((ndirs,nrows))
funcs_discrete = np.zeros((ndirs,nrows))
percent_continuous = np.zeros((ndirs,nrows))
time_continuous = np.zeros((ndirs,nrows))
funcs_continuous = np.zeros((ndirs,nrows))
opt_discrete = np.zeros((ndirs,nrows))
opt_continuous = np.zeros((ndirs,nrows))

for k in range(ndirs):
    rows,percent_increase,start_aep,opt_aep,time,funcs = read_layout_file("/Users/astanley/Projects/active_projects/stanley2021-yaw-optimization/grid_layout/discrete/discrete_%sdir_20yaw.txt"%dirs[k],TURBS=False)
    rows,percent_increase_c,start_aep_c,opt_aep_c,time_c,funcs_c = read_layout_file("/Users/astanley/Projects/active_projects/stanley2021-yaw-optimization/grid_layout/continuous/continuous_%sdir.txt"%dirs[k],TURBS=False)
    
    percent_discrete[k,:] = percent_increase[:]
    percent_continuous[k,:] = percent_increase_c[:]
    time_discrete[k,:] = time[:]
    time_continuous[k,:] = time_c[:]
    opt_discrete[k,:] = opt_aep[:]
    opt_continuous[k,:] = opt_aep_c[:]

plt.figure(figsize=(6,4))
ax1 = plt.subplot(231)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
ax2 = plt.subplot(232)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
ax3 = plt.subplot(233)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
ax4 = plt.subplot(234)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
ax5 = plt.subplot(235)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
ax6 = plt.subplot(236)
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
ax5.spines['right'].set_visible(False)
ax5.spines['top'].set_visible(False)
ax6.spines['right'].set_visible(False)
ax6.spines['top'].set_visible(False)

print(percent_discrete)
ax1.plot(rows,percent_continuous[0,:],"o")
ax1.plot(rows,percent_discrete[0,:],"o")
ax1.set_title("270 degrees",fontsize=8)

ax2.plot(rows,percent_continuous[1,:],"o",label="continuous")
ax2.plot(rows,percent_discrete[1,:],"o",label="Boolean")
ax2.set_title("285 degrees",fontsize=8)
ax2.legend(fontsize=8)

ax3.plot(rows,percent_continuous[2,:],"o")
ax3.plot(rows,percent_discrete[2,:],"o")
ax3.set_title("300 degrees",fontsize=8)

ax4.plot(rows,percent_continuous[3,:],"o")
ax4.plot(rows,percent_discrete[3,:],"o")
ax4.set_title("315 degrees",fontsize=8)

ax5.plot(rows,percent_continuous[4,:],"o")
ax5.plot(rows,percent_discrete[4,:],"o")
ax5.set_title("330 degrees",fontsize=8)

ax6.plot(rows,percent_continuous[5,:],"o")
ax6.plot(rows,percent_discrete[5,:],"o")
ax6.set_title("345 degrees",fontsize=8)


# ax1.plot(nturbs[0:ind],pd[0:ind],"o")
# ax1.plot(nturbs_c[0:ind],pc[0:ind],"o")
# ax1.set_ylim(0,5)
# ax1.set_ylabel("% power increase\nfrom baseline",fontsize=8)


# ax2.plot(nturbs[0:ind],oc[0:ind]/od[0:ind],"o")
# ax2.set_ylabel("opt power continuous/\nopt power Boolean",fontsize=8)

# ax3.plot(nturbs[0:ind],td[0:ind],"o")
# ax3.plot(nturbs_c[0:ind],tc[0:ind],"o")
# ax3.set_ylabel("time to run\noptimization (s)",fontsize=8)
# ax3.set_xlabel("number of turbines",fontsize=8)
# # ax3.set_ylabel("time continuous/\ntime boolean)",fontsize=8)

# ax4.plot(nturbs[0:ind],tc[0:ind]/td[0:ind],"o")
# # ax4.set_ylim(0,180)
# ax4.set_ylabel("time continuous/\ntime Boolean",fontsize=8)
# ax4.set_xlabel("number of turbines",fontsize=8)


ax1.set_xticks((3,4,5,6,7,8,9,10))
ax2.set_xticks((3,4,5,6,7,8,9,10))
ax3.set_xticks((3,4,5,6,7,8,9,10))
ax4.set_xticks((3,4,5,6,7,8,9,10))
ax5.set_xticks((3,4,5,6,7,8,9,10))
ax6.set_xticks((3,4,5,6,7,8,9,10))

ax1.set_ylim(0,71)
ax2.set_ylim(-0.1,0.1)
ax3.set_ylim(0,3.9)
ax4.set_ylim(0,30)
ax5.set_ylim(-0.1,0.1)
ax6.set_ylim(-0.3,1.8)

ax1.set_ylabel("% power increase\nfrom baseline",fontsize=8)
ax4.set_ylabel("% power increase\nfrom baseline",fontsize=8)
ax4.set_xlabel("number of grid rows",fontsize=8)
ax5.set_xlabel("number of grid rows",fontsize=8)
ax6.set_xlabel("number of grid rows",fontsize=8)



plt.suptitle("varied wind direction for a grid of turbines: percent improvement",fontsize=8)
plt.subplots_adjust(top=0.89,left=0.14,right=0.99,bottom=0.15,
            wspace=0.3,hspace=0.4)


plt.savefig("figures/grid_percent.pdf",transparent=True)

plt.show()



