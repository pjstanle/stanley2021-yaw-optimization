from logging import error
import matplotlib.pyplot as plt
import numpy as np

baseline_power_array = np.array([2.06644447e+07, 1.94768089e+07, 2.09754256e+07, 1.99239946e+07,
       2.17366984e+07, 1.64033173e+07, 9.98264320e+06, 1.43146866e+07,
       2.36452400e+07, 2.43949370e+07, 3.86653745e+07, 3.66651105e+07,
       2.88596645e+07, 3.38766608e+07, 3.44465821e+07, 2.71088134e+07,
       2.23597872e+07, 1.26156795e+07, 1.30364902e+07, 1.96460574e+07,
       1.59302084e+07, 7.84429926e+06, 1.10546971e+07, 2.73894373e+01,
       2.73894421e+01, 2.73895015e+01, 1.64138181e+07, 1.73550710e+07,
       1.74394784e+07, 1.88145139e+07, 2.22626346e+07, 3.42589182e+07,
       5.56008137e+07, 4.86203301e+07, 4.47219622e+07, 3.92493500e+07,
       3.53428396e+07, 3.90076989e+07, 5.10082208e+07, 5.77644147e+07,
       7.81314529e+07, 7.47634976e+07, 4.57769914e+07, 5.86779170e+07,
       8.80261524e+07, 7.36435240e+07, 6.68260328e+07, 5.59211721e+07,
       3.76499858e+07, 4.12906035e+07, 3.72294969e+07, 4.13524512e+07,
       3.39920173e+07, 2.11100263e+07, 1.79287950e+07, 2.79343544e+07,
       3.01009554e+07, 2.93699867e+07, 3.89641426e+07, 3.25909228e+07,
       2.98179954e+07, 3.45576654e+07, 3.50074451e+07, 3.85023725e+07,
       4.21551960e+07, 2.51366987e+07, 1.95288993e+07, 3.22559121e+07,
       3.21395030e+07, 2.82436903e+07, 2.30684010e+07, 2.82844209e+07])

optimized_boolean = np.array([2.10782973e+07, 1.99704861e+07, 2.09792411e+07, 1.99445070e+07,
       2.16498923e+07, 1.63074884e+07, 1.21643736e+07, 1.73355534e+07,
       2.36542790e+07, 2.43650053e+07, 3.85804629e+07, 3.66258474e+07,
       3.04172263e+07, 3.38307340e+07, 3.44392825e+07, 2.70723377e+07,
       2.22205129e+07, 1.31747257e+07, 1.67303160e+07, 2.02256648e+07,
       1.59013825e+07, 7.85077378e+06, 1.10171107e+07, 2.73719861e+01,
       2.73719903e+01, 2.73720499e+01, 1.64806849e+07, 1.73464279e+07,
       1.73810852e+07, 1.91293584e+07, 2.93713913e+07, 3.79772355e+07,
       5.56061663e+07, 4.85406481e+07, 4.48334721e+07, 3.92354123e+07,
       3.58758067e+07, 4.06530232e+07, 5.09235469e+07, 5.79749184e+07,
       7.80800434e+07, 7.45638794e+07, 5.12081289e+07, 6.98744921e+07,
       8.85459532e+07, 7.35119368e+07, 6.67814400e+07, 5.57991248e+07,
       3.93857534e+07, 4.14665893e+07, 3.71929237e+07, 4.13302123e+07,
       3.39175060e+07, 2.20845195e+07, 2.24363008e+07, 2.92882571e+07,
       3.00493688e+07, 2.93086358e+07, 3.89840945e+07, 3.26562191e+07,
       3.11771250e+07, 3.46076158e+07, 3.51568927e+07, 3.84851406e+07,
       4.20481608e+07, 2.54935557e+07, 2.60254470e+07, 3.56751266e+07,
       3.21044813e+07, 2.81905062e+07, 2.31213914e+07, 2.81854079e+07])


optimized_continuous = np.array([2.10819137e+07, 2.03799691e+07, 2.10006022e+07, 2.01955257e+07,
       2.17524534e+07, 1.64033173e+07, 1.22598316e+07, 1.74997355e+07,
       2.40122173e+07, 2.43949370e+07, 3.89670608e+07, 3.66651105e+07,
       3.05835163e+07, 3.41320270e+07, 3.46830177e+07, 2.71212516e+07,
       2.23597872e+07, 1.26156795e+07, 1.67696481e+07, 2.06686506e+07,
       1.59536471e+07, 7.87162979e+06, 1.11153435e+07, 2.73894373e+01,
       2.73894421e+01, 2.73895015e+01, 1.66634588e+07, 1.74169607e+07,
       1.74434479e+07, 1.88145139e+07, 2.86019897e+07, 3.85636864e+07,
       5.59742743e+07, 4.86374214e+07, 4.51891862e+07, 3.93787900e+07,
       3.61017541e+07, 4.10398680e+07, 5.11007056e+07, 5.84580820e+07,
       7.82650972e+07, 7.47634976e+07, 5.18710269e+07, 7.07328752e+07,
       8.95825209e+07, 7.36634902e+07, 6.74100008e+07, 5.59211721e+07,
       3.95549164e+07, 4.17582073e+07, 3.74760337e+07, 4.14660630e+07,
       3.39920173e+07, 2.17733653e+07, 2.28429777e+07, 2.96145224e+07,
       3.01399644e+07, 2.94607495e+07, 3.92097772e+07, 3.26211509e+07,
       3.14648000e+07, 3.47861178e+07, 3.53917728e+07, 3.86261111e+07,
       4.21696622e+07, 2.51366987e+07, 2.61130813e+07, 3.63180490e+07,
       3.23356816e+07, 2.82575176e+07, 2.33323883e+07, 2.83328159e+07])


wf = np.array([1.178129090726009499e-02,1.099587151344275440e-02,9.606283355150539369e-03,1.212365320712919213e-02,
        1.047225858423119459e-02,1.006947940791461105e-02,9.686839190413855730e-03,1.000906253146712291e-02,
        1.037156379015205000e-02,1.121740006041687700e-02,1.522505286476689111e-02,1.562783204108347465e-02,
        1.574866579397845093e-02,1.705769811700735133e-02,1.935353942201188324e-02,1.419796596515960144e-02,
        1.206323633068170399e-02,1.202295841305004581e-02,1.321115698318396994e-02,1.746047729332393661e-02,
        1.729936562279730042e-02,1.439935555331789407e-02,7.874332896989225464e-03,0.000000000000000000e+00,
        2.013895881582922239e-05,0.000000000000000000e+00,3.423622998690967569e-04,3.564595710401772394e-03,
        7.189608297251032058e-03,8.800725002517370554e-03,1.135837277212768150e-02,1.415768804752794326e-02,
        1.669519685832242598e-02,1.631255664082166892e-02,1.317087906555231176e-02,1.091531567817943804e-02,
        9.485449602255563092e-03,1.010975732554626923e-02,1.188198570133924131e-02,1.260698821870909203e-02,
        1.588963850568925543e-02,1.770214479911388569e-02,2.042090423925083109e-02,2.279730137951867935e-02,
        2.954385258282146709e-02,3.028899405900714950e-02,2.698620481321115788e-02,2.215285469741214500e-02,
        2.124660155069982986e-02,1.828617460477293191e-02,1.661464102305910615e-02,1.901117712214278610e-02,
        1.905145503977444255e-02,1.639311247608498529e-02,1.762158896385056933e-02,1.653408518779578978e-02,
        1.445977242976538048e-02,1.403685429463296698e-02,1.657436310542744970e-02,1.562783204108347465e-02,
        1.534588661766186739e-02,1.752089416977142128e-02,1.597019434095257179e-02,1.510421911187191657e-02,
        1.452018930621286862e-02,1.345282448897392076e-02,1.478199577081864939e-02,1.339240761252643262e-02,
        1.105628838989024254e-02,1.045211962541536636e-02,1.162017923673346054e-02,1.105628838989024254e-02])

wd = np.array([0.000000000000000000e+00,5.000000000000000000e+00,1.000000000000000000e+01,1.500000000000000000e+01,
                    2.000000000000000000e+01,2.500000000000000000e+01,3.000000000000000000e+01,3.500000000000000000e+01,
                    4.000000000000000000e+01,4.500000000000000000e+01,5.000000000000000000e+01,5.500000000000000000e+01,
                    6.000000000000000000e+01,6.500000000000000000e+01,7.000000000000000000e+01,7.500000000000000000e+01,
                    8.000000000000000000e+01,8.500000000000000000e+01,9.000000000000000000e+01,9.500000000000000000e+01,
                    1.000000000000000000e+02,1.050000000000000000e+02,1.100000000000000000e+02,1.150000000000000000e+02,
                    1.200000000000000000e+02,1.250000000000000000e+02,1.300000000000000000e+02,1.350000000000000000e+02,
                    1.400000000000000000e+02,1.450000000000000000e+02,1.500000000000000000e+02,1.550000000000000000e+02,
                    1.600000000000000000e+02,1.650000000000000000e+02,1.700000000000000000e+02,1.750000000000000000e+02,
                    1.800000000000000000e+02,1.850000000000000000e+02,1.900000000000000000e+02,1.950000000000000000e+02,
                    2.000000000000000000e+02,2.050000000000000000e+02,2.100000000000000000e+02,2.150000000000000000e+02,
                    2.200000000000000000e+02,2.250000000000000000e+02,2.300000000000000000e+02,2.350000000000000000e+02,
                    2.400000000000000000e+02,2.450000000000000000e+02,2.500000000000000000e+02,2.550000000000000000e+02,
                    2.600000000000000000e+02,2.650000000000000000e+02,2.700000000000000000e+02,2.750000000000000000e+02,
                    2.800000000000000000e+02,2.850000000000000000e+02,2.900000000000000000e+02,2.950000000000000000e+02,
                    3.000000000000000000e+02,3.050000000000000000e+02,3.100000000000000000e+02,3.150000000000000000e+02,
                    3.200000000000000000e+02,3.250000000000000000e+02,3.300000000000000000e+02,3.350000000000000000e+02,
                    3.400000000000000000e+02,3.450000000000000000e+02,3.500000000000000000e+02,3.550000000000000000e+02])

plt.figure(figsize=(5.25,2.5))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

# ax1.plot(wd,baseline_power_array,label="baseline")
ax1.plot(wd,(optimized_continuous-baseline_power_array)/baseline_power_array*100, label="continuous")
ax1.plot(wd,(optimized_boolean-baseline_power_array)/baseline_power_array*100,"--",label="boolean")

ax2.plot(wd,wf*(optimized_continuous-baseline_power_array)/baseline_power_array*100, label="continuous")
ax2.plot(wd,wf*(optimized_boolean-baseline_power_array)/baseline_power_array*100,"--",label="boolean")

ax2.legend(fontsize=8,loc=2)

ax1.tick_params(axis='both', which='major', labelsize=8)
ax1.tick_params(axis='both', which='minor', labelsize=8)

ax2.tick_params(axis='both', which='major', labelsize=8)
ax2.tick_params(axis='both', which='minor', labelsize=8)

ax1.set_xlabel("wind direction", fontsize=8)
ax2.set_xlabel("wind direction", fontsize=8)

ax1.set_ylabel("percent power improvement", fontsize=8)
ax2.set_ylabel("frequency weighted\npercent power improvement", fontsize=8)


plt.subplots_adjust(left=0.1,right=0.99,top=0.98,bottom=0.2,wspace=0.4)


dy = 0.3
dx = 0.1
limx = ax1.get_xlim()
limy = ax1.get_ylim()
ax1.text(limx[0]+dx*(limx[1]-limx[0]),limy[1]-0.1*(limy[1]-limy[0]),"a",fontsize=10,weight="bold")
limx = ax2.get_xlim()
limy = ax2.get_ylim()
ax2.text(limx[0]+dx*(limx[1]-limx[0]),limy[1]-0.3*(limy[1]-limy[0]),"b",fontsize=10,weight="bold")


plt.savefig("figures/amalia_powers.pdf",transparent=True)
plt.show()