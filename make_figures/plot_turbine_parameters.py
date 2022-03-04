import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, radians
import floris.tools as wfct

D = 240.0
H = 150.0
rho = 1.225
A = 0.25*np.pi*D**2

Cp = np.array([
            0.09331,
            0.25314,
            0.33415,
            0.38052,
            0.39738,
            0.41089,
            0.42102,
            0.44200,
            0.44592,
            0.44907,
            0.45054,
            0.45122,
            0.45189,
            0.45302,
            0.45393,
            0.45465,
            0.45476,
            0.45482,
            0.45485,
            0.45488,
            0.45489,
            0.45491,
            0.45492,
            0.45491,
            0.45492,
            0.45498,
            0.45501,
            0.45504,
            0.45504,
            0.45505,
            0.45507,
            0.45513,
            0.45512,
            0.45245,
            0.43988,
            0.43742,
            0.43498,
            0.43256,
            0.43016,
            0.42968,
            0.42944,
            0.42932,
            0.42920,
            0.42908,
            0.42903,
            0.42777,
            0.41610,
            0.40485,
            0.37845,
            0.35430,
            0.33216,
            0.31182,
            0.24526,
            0.19636,
            0.15964,
            0.10052,
            0.06733,
            0.04728,
            0.03447
          ])
Ct = np.array([
            0.819748943,
            0.801112031,
            0.808268424,
            0.821910918,
            0.822876237,
            0.823265981,
            0.830989358,
            0.834932456,
            0.833618598,
            0.83180478,
            0.829011103,
            0.826909201,
            0.824740997,
            0.820429675,
            0.816176257,
            0.811200233,
            0.809740903,
            0.808780765,
            0.808102306,
            0.807566626,
            0.807251977,
            0.80662442,
            0.806495512,
            0.806806173,
            0.806651158,
            0.805469658,
            0.804571567,
            0.803949121,
            0.803904895,
            0.803708734,
            0.80345211,
            0.801706154,
            0.801777393,
            0.768657554,
            0.70731525,
            0.698507743,
            0.690211963,
            0.682335591,
            0.674835939,
            0.673371183,
            0.672646111,
            0.672283185,
            0.671921569,
            0.671564033,
            0.671386994,
            0.667639697,
            0.635292304,
            0.607277698,
            0.548965866,
            0.501379105,
            0.460982977,
            0.425965654,
            0.32116631,
            0.2511023,
            0.201415182,
            0.125653944,
            0.08506697,
            0.061026446,
            0.045814967
          ])
Ws = np.array([
            2.999999831,
            3.499999916,
            4,
            4.500000084,
            4.750000126,
            5.000000169,
            5.249999874,
            5.999999663,
            6.199999966,
            6.40000027,
            6.499999747,
            6.55000016,
            6.599999899,
            6.700000051,
            6.800000202,
            6.900000354,
            6.919999845,
            6.929999928,
            6.94000001,
            6.950000093,
            6.960000175,
            6.969999584,
            6.980000341,
            6.989999749,
            6.999999831,
            7.499999916,
            8,
            8.500000084,
            9.000000169,
            9.500000253,
            10.00000034,
            10.2499997,
            10.49999975,
            10.60000057,
            10.70000005,
            10.72000022,
            10.73999971,
            10.76000055,
            10.78000004,
            10.78400034,
            10.78600049,
            10.78699989,
            10.78799997,
            10.78899937,
            10.78950042,
            10.8000002,
            10.89999968,
            10.99999983,
            11.24999987,
            11.50000059,
            11.75000063,
            11.99999933,
            12.99999949,
            13.99999966,
            14.99999983,
            17.50000025,
            20.00000067,
            22.49999975,
            24.99999882
          ])

# plt.subplots_adjust(top=0.94,bottom=0.01,right=0.99,left=0.01,wspace=0.05)

# plt.savefig("grid_layouts.png")



fig = plt.figure(figsize=[6,2])


ax = plt.subplot(131)
ax.set_title("dimensions",fontsize=8)
bladeX = np.array([3.,7.,10.,15.,20.,25.,30.,35.,30.,25.,20.,15.,10.,5.,3.,3.])
bladeY = np.array([0.,0.,0.8,1.5,1.7,1.9,2.1,2.3,2.4,2.4,2.4,2.4,2.4,2.4,2.4,0.])-1.5


N = 12
r1 = 5
r2 = 3

H =150.0
D = 240.0
R = D/2.0
d = np.array([6.3,5.5,4.])*D/200.0

circle1 = plt.Circle((0.,H), R, color='C0', fill=False, linestyle = '--', linewidth=1.2*1.5)
ax.add_artist(circle1)

c1 = R/35.

px1 = np.array([0.-d[0]/2,0.-d[1]/2,0.-d[2]/2,0.+d[2]/2,0.+d[1]/2,0.+d[0]/2,0.-d[0]/2])
py1 = np.array([0,H/2,H-3.*c1,H-3.*c1,H/2,0,0])
ax.plot(px1,py1,color='C0', linewidth=1.2*1.5)

#add blades
hub1 = plt.Circle((0.,H), 3*c1, color='C0', fill=False, linewidth=1*1.5)
ax.add_artist(hub1)

angle1 = 92.0

blade1X = bladeX*cos(radians(angle1))-bladeY*sin(radians(angle1))
blade1Y = bladeX*sin(radians(angle1))+bladeY*cos(radians(angle1))

blade2X = bladeX*cos(radians(angle1+120.))-bladeY*sin(radians(angle1+120.))
blade2Y = bladeX*sin(radians(angle1+120.))+bladeY*cos(radians(angle1+120.))

blade3X = bladeX*cos(radians(angle1+240.))-bladeY*sin(radians(angle1+240.))
blade3Y = bladeX*sin(radians(angle1+240.))+bladeY*cos(radians(angle1+240.))

ax.plot(blade1X*c1+0., blade1Y*c1+H, linewidth=1*1.5, color='C0')
ax.plot(blade2X*c1+0., blade2Y*c1+H, linewidth=1*1.5, color='C0')
ax.plot(blade3X*c1+0., blade3Y*c1+H, linewidth=1*1.5, color='C0')

# plot rotor diameter text
rot_angle = 50.0
s = np.sin(np.deg2rad(rot_angle))
c = np.cos(np.deg2rad(rot_angle))
ax.plot([-R*c,R*c],[-R*s+H,R*s+H],"-",color="k")

s2 = np.sin(np.deg2rad(rot_angle+90))
c2 = np.cos(np.deg2rad(rot_angle+90))
L = 10
ax.plot([-R*c-L*c2,-R*c+L*c2],[-R*s+H-L*s2,-R*s+H+L*s2],"-",color="k")
ax.plot([R*c-L*c2,R*c+L*c2],[R*s+H-L*s2,R*s+H+L*s2],"-",color="k")

ax.text(125.0,H+95,"%s m"%round(D),horizontalalignment="center",fontsize=8)

# plot hub height text
ax.plot([-R-20,-R-20],[0,H],"-k")
ax.plot([-R-20-L,-R-20+L],[0,0],"-k")
ax.plot([-R-20-L,-R-20+L],[H,H],"-k")

ax.text(-R-65,H/2,"%s m"%round(H),verticalalignment="center",horizontalalignment="center",fontsize=8)

ax.axis('square')
ax.axis('off')
ax.set_xlim(-150-L,120)
ax.set_ylim(-5,280)
    
ax2 = plt.subplot(132)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.plot(Ws,Cp,color="C1",linewidth=2)

ax3 = plt.subplot(133)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.plot(Ws,Ct,color="C3",linewidth=2)

ax2.set_xlabel("wind speed",fontsize=8)
ax3.set_xlabel("wind speed",fontsize=8)
ax2.set_ylabel("power coefficient",fontsize=8)
ax3.set_ylabel("thrust coefficient",fontsize=8)


dy = 0.02
dx = 0.05
limx = ax.get_xlim()
limy = ax.get_ylim()
ax.text(limx[0]+dx*(limx[1]-limx[0]),limy[1]-dy*(limy[1]-limy[0]),"a",fontsize=10,weight="bold")
limx = ax2.get_xlim()
limy = ax2.get_ylim()
ax2.text(limx[0]+dx*(limx[1]-limx[0]),limy[1]-dy*(limy[1]-limy[0]),"b",fontsize=10,weight="bold")
limx = ax3.get_xlim()
limy = ax3.get_ylim()
ax3.text(limx[0]+dx*(limx[1]-limx[0]),limy[1]-dy*(limy[1]-limy[0]),"c",fontsize=10,weight="bold")


plt.subplots_adjust(bottom=0.2,left=0.06,right=0.99,top=0.9,wspace=0.5)

plt.savefig("figures/turbine_parameters.pdf",transparent=True)
plt.show()