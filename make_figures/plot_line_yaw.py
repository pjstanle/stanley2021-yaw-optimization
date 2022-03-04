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


yaw_angles = [5,10,15,20,25,30]
percent_array = np.zeros((len(yaw_angles),5))


for i in range(len(yaw_angles)):

    nturbs,percent_discrete,start_aep,opt_discrete,time_discrete,funcs_discrete = read_layout_file("/Users/astanley/Projects/active_projects/stanley2021-yaw-optimization/line_layout/discrete/discrete_3spacing_%syaw.txt"%yaw_angles[i])
    percent_array[i,:] = percent_discrete[:]

plt.figure(figsize=(6,2.5))
ax1 = plt.subplot(131)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

ax1.plot(nturbs,percent_array[0,:],"--",label="5",color="C0")
ax1.plot(nturbs,percent_array[1,:],label="10",color="C1")
ax1.plot(nturbs,percent_array[2,:],"--",label="15",color="C3")
ax1.plot(nturbs,percent_array[3,:],label="20",color="C0")
ax1.plot(nturbs,percent_array[4,:],"--",label="25",color="C1")
ax1.plot(nturbs,percent_array[5,:],label="30",color="C3")

# ax1.set_ylim(0,330)


for i in range(len(yaw_angles)):

    nturbs,percent_discrete,start_aep,opt_discrete,time_discrete,funcs_discrete = read_layout_file("/Users/astanley/Projects/active_projects/stanley2021-yaw-optimization/line_layout/discrete/discrete_5spacing_%syaw.txt"%yaw_angles[i])
    percent_array[i,:] = percent_discrete[:]

ax2 = plt.subplot(132)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

ax2.plot(nturbs,percent_array[0,:],"--",label="5",color="C0")
ax2.plot(nturbs,percent_array[1,:],label="10",color="C1")
ax2.plot(nturbs,percent_array[2,:],"--",label="15",color="C3")
ax2.plot(nturbs,percent_array[3,:],label="20",color="C0")
ax2.plot(nturbs,percent_array[4,:],"--",label="25",color="C1")
ax2.plot(nturbs,percent_array[5,:],label="30",color="C3")

# ax2.set_ylim(0,103)


for i in range(len(yaw_angles)):

    nturbs,percent_discrete,start_aep,opt_discrete,time_discrete,funcs_discrete = read_layout_file("/Users/astanley/Projects/active_projects/stanley2021-yaw-optimization/line_layout/discrete/discrete_8spacing_%syaw.txt"%yaw_angles[i])
    percent_array[i,:] = percent_discrete[:]

ax3 = plt.subplot(133)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)

ax3.plot(nturbs,percent_array[0,:],"--",label="5",color="C0")
ax3.plot(nturbs,percent_array[1,:],label="10",color="C1")
ax3.plot(nturbs,percent_array[2,:],"--",label="15",color="C3")
ax3.plot(nturbs,percent_array[3,:],label="20",color="C0")
ax3.plot(nturbs,percent_array[4,:],"--",label="25",color="C1")
ax3.plot(nturbs,percent_array[5,:],label="30",color="C3")

# ax3.set_ylim(0,44)



ax1.set_xlabel("number of turbines",fontsize=8)
ax1.set_ylabel("% power increase\nfrom baseline",fontsize=8)
ax1.set_xticks((10,20,30,40,50))

ax2.set_xlabel("number of turbines",fontsize=8)
ax2.set_xticks((10,20,30,40,50))

ax3.set_xlabel("number of turbines",fontsize=8)
ax3.set_xticks((10,20,30,40,50))



leg = ax3.legend(bbox_to_anchor=(1, 1), ncol=1, prop={'size': 8})
leg.set_title('Boolean yaw\n(degrees)',prop={'size':8})



ax1.set_title("3 D spacing",fontsize=8)
ax2.set_title("5 D spacing",fontsize=8)
ax3.set_title("8 D spacing",fontsize=8)

plt.suptitle("In-line Boolean yaw angles",fontsize=8)
plt.subplots_adjust(top=0.84,left=0.12,right=0.85,bottom=0.15)

# plt.savefig("figures/line_yaw_angle_3.pdf",transparent=True)

plt.show()



