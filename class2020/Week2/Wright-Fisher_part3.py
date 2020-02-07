#!/usr/bin/env python3

import sys
import numpy as np
import scipy as sc
import seaborn as sns
import matplotlib.pyplot as plt

def simulation(p, N, s, repetitions=1000):
    N = int(2*N)
    n1 = np.ones(repetitions) * (N*p)
    T = np.empty_like(n1)
    update = (n1 > 0) & (n1 < N)
    t = 0
    
    while update.any():
        t += 1
        p = n1 * (1 + s) / (N + n1 * s)
        n1[update] = np.random.binomial(N, p[update])
        T[update] = t
        update = (n1 > 0) & (n1 < N)

    return n1 == N, T

print("Fixate %", simulation(p=0.5, N=100, s=0)[0].mean())

fixations, times = simulation(p=0.5, N=100, s=0, repetitions=1000)
fixation_prob = fixations.mean()
fixation_time = times[fixations].mean()


fixation_time_3 = {}
allele_freqs = [0.2,0.4,0.6,0.8]
for allele_freq in allele_freqs:
    fixation_time_3[allele_freq] = []
    for i in range(100):
        fixation_time_3[allele_freq].append(simulation(p=allele_freq, N=100, s=0, repetitions=1000))
        
for allele_freq in allele_freqs:
    fixation_time_3[allele_freq] = []
    for i in range(100):
        fixation_time_3[allele_freq].append(simulation(p=allele_freq, N=100, s=0, repetitions=1000))
mean3 = []
std_dev3 = []
for allele_freq in allele_freqs:
    mean3.append(np.mean(fixation_time_3[allele_freq]))
    std_dev3.append(np.std(fixation_time_3[allele_freq]))

# fig,ax = plt.subplots()
# ax.bar([x for x in range(1,len(allele_freqs)+1)], mean3, yerr= std_dev3)
# ax.set_xlabel("Starting Allele Frequency")
# ax.set_xticks([x for x in range(1,len(allele_freqs)+1)])
# ax.set_xticklabels(["0.2", "0.4", "0.6", "0.8"])
# ax.set_ylabel("Generations to Fixation")
# plt.title("Plot 3")
# fig.savefig("varyingallelefreq.png")
# plt.close



#part 4
fixation_times4 = {}
selection_coeffs = [0,0.2,0.4,0.6,0.8,1]
for selection_coeff in selection_coeffs:
    fixation_times4[selection_coeff] = []
    for i in range(100):
        fixation_times4[selection_coeff].append(simulation(p=0.5, N=100, s=selection_coeff, repetitions=1000))
mean4 = []
std_dev4 = []
for selection_coeff in selection_coeffs:
    mean4.append(np.mean(fixation_times4[selection_coeff]))
    std_dev4.append(np.std(fixation_times4[selection_coeff]))
fig,ax = plt.subplots()
ax.bar([x for x in range(1,len(selection_coeffs)+1)], mean4, yerr= std_dev4)
ax.set_xlabel("Starting Selection Coefficient")
ax.set_xticks([x for x in range(1,len(selection_coeffs)+1)])
ax.set_xticklabels(["0","0.2", "0.4", "0.6", "0.8","1"])
ax.set_ylabel("Generations to Fixation")
plt.title("Plot 4")
fig.savefig("varyingselection_coeff.png")
plt.show()
