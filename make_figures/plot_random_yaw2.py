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
percent_array = np.zeros((len(yaw_angles),10))
nseeds = 7

for k in range(nseeds):
    for i in range(len(yaw_angles)):

        nturbs,percent_discrete,start_aep,opt_discrete,time_discrete,funcs_discrete = read_layout_file("/Users/astanley/Projects/active_projects/stanley2021-yaw-optimization/random_layout/discrete/discrete_seed%s_%syaw.txt"%(k,yaw_angles[i]))
        percent_array[i,:] += percent_discrete[:]

percent_array = percent_array/nseeds

plt.figure(figsize=(4,2.5))
ax1 = plt.subplot(111)

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

# ax1.plot(nturbs,percent_array[0,:],label="5")
# ax1.plot(nturbs,percent_array[1,:],label="10")
# ax1.plot(nturbs,percent_array[2,:],label="15")
# ax1.plot(nturbs,percent_array[3,:],label="20")
# ax1.plot(nturbs,percent_array[4,:],label="25")
# ax1.plot(nturbs,percent_array[5,:],label="30")

# ax1.plot(nturbs,percent_array[0,:],"--",label="5",color="C0")
# ax1.plot(nturbs,percent_array[1,:],label="10",color="C1")
# ax1.plot(nturbs,percent_array[2,:],"--",label="15",color="C3")
# ax1.plot(nturbs,percent_array[3,:],label="20",color="C0")
# ax1.plot(nturbs,percent_array[4,:],"--",label="25",color="C1")
# ax1.plot(nturbs,percent_array[5,:],label="30",color="C3")
ax1.plot(yaw_angles,percent_array[:,0],"--",label="10",color="C0")
ax1.plot(yaw_angles,percent_array[:,1],label="20",color="C1")
ax1.plot(yaw_angles,percent_array[:,2],"--",label="30",color="C3")
ax1.plot(yaw_angles,percent_array[:,3],label="40",color="C0")
ax1.plot(yaw_angles,percent_array[:,4],"--",label="50",color="C1")

# ax1.set_ylim(0,103)
ax1.set_xlabel("Boolean yaw angle\n(degrees)",fontsize=8)
ax1.set_ylabel("% power increase\nfrom baseline",fontsize=8)
ax1.set_xticks((5,10,15,20,25,30))
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
leg = ax1.legend(bbox_to_anchor=(1, 1), ncol=1, prop={'size': 8})
leg.set_title('number of\nturbines',prop={'size':8})



plt.title("Random turbine layouts",fontsize=8)
plt.subplots_adjust(top=0.9,left=0.18,right=0.75,bottom=0.2)

plt.savefig("figures/random_yaw_angle_redone.pdf",transparent=True)

plt.show()



