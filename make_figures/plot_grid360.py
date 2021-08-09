from logging import error
import matplotlib.pyplot as plt
import numpy as np
import csv


def read_layout_file(filename):

    wind_direction = np.array([])
    percent_increase = np.array([])
    start_aep = np.array([])
    opt_aep = np.array([])
    time = np.array([])
    funcs = np.array([])

    with open(filename) as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) > 0:
                if row[0].split()[0] == "wind_direction":
                    wind_direction = np.append(wind_direction,float(row[0].split()[2]))
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

    return wind_direction,percent_increase,start_aep,opt_aep,time,funcs

wd_c,percent_c,start_c,opt_c,time_c,funcs_c = read_layout_file("/Users/astanley/Projects/active_projects/stanley2021-yaw-optimization/grid_layout/continuous360/continuous_5rows.txt")
wd_d,percent_d,start_d,opt_d,time_d,funcs_d = read_layout_file("/Users/astanley/Projects/active_projects/stanley2021-yaw-optimization/grid_layout/discrete360/discrete_5rows.txt")


plt.figure(figsize=(4,4))
ax1 = plt.subplot(111)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

print(wd_d)
print(opt_d)
ax1.plot(wd_c,start_c,color="C0")
ax1.plot(wd_c,opt_c,color="C1")
ax1.plot(wd_c,opt_d,color="C3")

# ax1.set_title("270 degrees",fontsize=8)



# # ax1.plot(nturbs[0:ind],pd[0:ind],"o")
# # ax1.plot(nturbs_c[0:ind],pc[0:ind],"o")
# # ax1.set_ylim(0,5)
# # ax1.set_ylabel("% power increase\nfrom baseline",fontsize=8)



# ax1.set_xticks((3,4,5,6,7,8,9,10))


# ax1.set_ylim(0,71)


# ax1.set_ylabel("% power increase\nfrom baseline",fontsize=8)

# plt.subplots_adjust(top=0.89,left=0.14,right=0.99,bottom=0.15,
#             wspace=0.3,hspace=0.4)


# plt.savefig("figures/grid_percent.pdf",transparent=True)

plt.show()



