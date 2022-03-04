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
    rows,percent_increase,start_aep,opt_aep,time,funcs = read_layout_file("../grid_layout/discrete/discrete_%sdir_20yaw.txt"%dirs[k],TURBS=False)
    rows,percent_increase_c,start_aep_c,opt_aep_c,time_c,funcs_c = read_layout_file("../grid_layout/continuous/continuous_%sdir.txt"%dirs[k],TURBS=False)
    
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
ax1.plot(rows,opt_continuous[0,:]/opt_discrete[0,:],"o",color="C3")
ax1.set_title("270 degrees",fontsize=8)

ax2.plot(rows,opt_continuous[1,:]/opt_discrete[1,:],"o",color="C3")
ax2.set_title("285 degrees",fontsize=8)

ax3.plot(rows,opt_continuous[2,:]/opt_discrete[2,:],"o",color="C3")
ax3.set_title("300 degrees",fontsize=8)

ax4.plot(rows,opt_continuous[3,:]/opt_discrete[3,:],"o",color="C3")
ax4.set_title("315 degrees",fontsize=8)

ax5.plot(rows,opt_continuous[4,:]/opt_discrete[4,:],"o",color="C3")
ax5.set_title("330 degrees",fontsize=8)

ax6.plot(rows,opt_continuous[5,:]/opt_discrete[5,:],"o",color="C3")
ax6.set_title("345 degrees",fontsize=8)

ax1.set_xticks((3,4,5,6,7,8,9,10))
ax2.set_xticks((3,4,5,6,7,8,9,10))
ax3.set_xticks((3,4,5,6,7,8,9,10))
ax4.set_xticks((3,4,5,6,7,8,9,10))
ax5.set_xticks((3,4,5,6,7,8,9,10))
ax6.set_xticks((3,4,5,6,7,8,9,10))

ax1.set_ylim(0.99,1.045)
ax2.set_ylim(0.99,1.045)
ax3.set_ylim(0.99,1.045)
ax4.set_ylim(0.99,1.045)
ax5.set_ylim(0.99,1.045)
ax6.set_ylim(0.99,1.045)

ax1.set_ylabel("opt power continuous/\nopt power Boolean",fontsize=8)
ax4.set_ylabel("opt power continuous/\nopt power Boolean",fontsize=8)
ax4.set_xlabel("number of grid rows",fontsize=8)
ax5.set_xlabel("number of grid rows",fontsize=8)
ax6.set_xlabel("number of grid rows",fontsize=8)



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
limx = ax5.get_xlim()
limy = ax5.get_ylim()
ax5.text(limx[0]+dx*(limx[1]-limx[0]),limy[1]-dy*(limy[1]-limy[0]),"e",fontsize=10,weight="bold")
limx = ax6.get_xlim()
limy = ax6.get_ylim()
ax6.text(limx[0]+dx*(limx[1]-limx[0]),limy[1]-dy*(limy[1]-limy[0]),"f",fontsize=10,weight="bold")

plt.suptitle("Varied wind direction for a grid of turbines: optimal power ratio",fontsize=8)
plt.subplots_adjust(top=0.89,left=0.14,right=0.99,bottom=0.15,
            wspace=0.3,hspace=0.4)


plt.savefig("figures/grid_aep_ratio.pdf",transparent=True)

plt.show()



