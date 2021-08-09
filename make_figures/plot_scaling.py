import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# mpl.rc('font', family = 'serif', serif = 'cmr10')
fig = plt.figure(figsize=[3.,2.5])
ax2 = plt.subplot(111)

ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.yaxis.set_ticks_position('left')
ax2.xaxis.set_ticks_position('bottom')

ax2.tick_params(axis='both', which='major', labelsize=8)
ax2.tick_params(axis='both', which='minor', labelsize=8)

dimvec2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
snopt_grad = np.array([31, 35, 36, 45, 64, 68, 157, 183, 195, 244])
slsqp_grad = np.array([33, 30, 43, 76, 135, 271, 535, 271, 445, 577])
snopt_fd = np.array([102, 248, 375, 1017, 3054, 6315, 60142, 151453, 212337, 776704])
slsqp_fd = np.array([84, 118, 227, 621, 1646, 5324, 16877, 36639, 46939, 152124])
dimvec = [2, 4, 8, 16, 32, 64]
alpso = np.array([1150, 32780, 108040, 488240, 2649760, 12301760])


ax2.set_xscale('log')
ax2.set_yscale('log')

ax2.plot(dimvec2,snopt_grad,'o',color='C0')
ax2.plot(dimvec2,snopt_fd,'o',color='C1')
ax2.plot(dimvec,alpso,'o',color='C3')
# ax2.set_xticks((1E1,1E2,1E3))
ax2.set_xticks((10,36000))
ax2.set_ylim(10,1E9)
# ax2.set_yticks((1E1,1E3,1E5,1E7))
# ax2.set_yticklabels((r'10$^1$',r'10$^3$',r'10$^5$',r'10$^7$'))

ax2.text(45, 20, 'analytic gradients',fontsize=8, color='C0')
ax2.text(45, 1*5e2, 'finite difference\ngradients',fontsize=8, color='C1')
ax2.text(30, 7e5, 'particle swarm',fontsize=8, color='C3')

ax2.set_ylabel('number of function\ncalls to optimize',fontsize=8)
ax2.set_xlabel('number of design variables',fontsize=8)

plt.minorticks_off()

plt.subplots_adjust(top = 0.94, bottom = 0.2, right = 0.98, left = 0.25,
            hspace = 0.6, wspace = 0.2)

# plt.savefig('figures/scaling.pdf',transparent=True)
plt.show()
