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
    filename = "../line_layout/discrete/discrete_3spacing_%syaw.txt"%yaw_angles[i]
    nturbs,percent_discrete,start_aep,opt_discrete,time_discrete,funcs_discrete = read_layout_file(filename)
    # nturbs,percent_discrete,start_aep,opt_discrete,time_discrete,funcs_discrete = read_layout_file("/Users/astanley/Projects/active_projects/stanley2021-yaw-optimization/line_layout/discrete/discrete_3spacing_%syaw.txt"%yaw_angles[i])
    percent_array[i,:] = percent_discrete[:]

plt.figure(figsize=(6,2.5))
ax1 = plt.subplot(131)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

ax1.plot(yaw_angles,percent_array[:,0],"--",label="10",color="C0")
ax1.plot(yaw_angles,percent_array[:,1],label="20",color="C1")
ax1.plot(yaw_angles,percent_array[:,2],"--",label="30",color="C3")
ax1.plot(yaw_angles,percent_array[:,3],label="40",color="C0")
ax1.plot(yaw_angles,percent_array[:,4],"--",label="50",color="C1")

# ax1.set_ylim(0,330)


for i in range(len(yaw_angles)):
    filename = "../line_layout/discrete/discrete_5spacing_%syaw.txt"%yaw_angles[i]
    nturbs,percent_discrete,start_aep,opt_discrete,time_discrete,funcs_discrete = read_layout_file(filename)
    # nturbs,percent_discrete,start_aep,opt_discrete,time_discrete,funcs_discrete = read_layout_file("/Users/astanley/Projects/finished_projects/stanley2021-yaw-optimization/line_layout/discrete/discrete_5spacing_%syaw.txt"%yaw_angles[i])
    percent_array[i,:] = percent_discrete[:]

ax2 = plt.subplot(132)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

ax2.plot(yaw_angles,percent_array[:,0],"--",label="10",color="C0")
ax2.plot(yaw_angles,percent_array[:,1],label="20",color="C1")
ax2.plot(yaw_angles,percent_array[:,2],"--",label="30",color="C3")
ax2.plot(yaw_angles,percent_array[:,3],label="40",color="C0")
ax2.plot(yaw_angles,percent_array[:,4],"--",label="50",color="C1")

# ax2.set_ylim(0,103)


for i in range(len(yaw_angles)):
    filename = "../line_layout/discrete/discrete_8spacing_%syaw.txt"%yaw_angles[i]
    nturbs,percent_discrete,start_aep,opt_discrete,time_discrete,funcs_discrete = read_layout_file(filename)
    # nturbs,percent_discrete,start_aep,opt_discrete,time_discrete,funcs_discrete = read_layout_file("/Users/astanley/Projects/active_projects/stanley2021-yaw-optimization/line_layout/discrete/discrete_8spacing_%syaw.txt"%yaw_angles[i])
    percent_array[i,:] = percent_discrete[:]

ax3 = plt.subplot(133)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)

ax3.plot(yaw_angles,percent_array[:,0],"--",label="10",color="C0")
ax3.plot(yaw_angles,percent_array[:,1],label="20",color="C1")
ax3.plot(yaw_angles,percent_array[:,2],"--",label="30",color="C3")
ax3.plot(yaw_angles,percent_array[:,3],label="40",color="C0")
ax3.plot(yaw_angles,percent_array[:,4],"--",label="50",color="C1")

# ax3.set_ylim(0,44)



ax1.set_xlabel("Boolean yaw angle\n(degrees)",fontsize=8)
ax1.set_ylabel("% power increase\nfrom baseline",fontsize=8)
ax1.set_xticks((5,10,15,20,25,30))

ax2.set_xlabel("Boolean yaw angle\n(degrees)",fontsize=8)
ax2.set_xticks((5,10,15,20,25,30))

ax3.set_xlabel("Boolean yaw angle\n(degrees)",fontsize=8)
ax3.set_xticks((5,10,15,20,25,30))



leg = ax3.legend(bbox_to_anchor=(1, 1), ncol=1, prop={'size': 8})
leg.set_title('number of\nturbines',prop={'size':8})



ax1.set_title("3 D spacing",fontsize=8)
ax2.set_title("5 D spacing",fontsize=8)
ax3.set_title("8 D spacing",fontsize=8)

dy = 0.02
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

plt.suptitle("Turbines in-line with wind",fontsize=8)
plt.subplots_adjust(top=0.84,left=0.12,right=0.85,bottom=0.2)

plt.savefig("figures/line_yaw_angle_redone.pdf",transparent=True)

plt.show()



