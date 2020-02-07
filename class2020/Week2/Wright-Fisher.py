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


w, h = plt.rcParams['figure.figsize']
fig, ax = plt.subplots()

sns.distplot(times[fixations], ax=ax)
ax.set_title("Histogram 1")
ax.axvline(times[fixations].mean(), color='k', ls='--')
ax.set(xlabel='Fixation time', ylabel='Frequency')
fig.savefig("Histogram")


repetitions = 100
s = 0
Nrange = np.logspace(1, 6, 10, dtype=np.uint64)
def fix_time_simulation(N):
    fixations, times = simulation(p=0.5, N=N, s=0, repetitions=100)
    fixation_time_mean = times[fixations].mean()
    fixation_time_std =  times[fixations].std(ddof=1) / np.sqrt(repetitions)
    return fixation_time_mean, fixation_time_std
fix_time_sim = np.array([
    fix_time_simulation(N=N)
    for N in Nrange
])
def fixation_time_plot(N, mean, sem):
    fig, ax = plt.subplots(1, 1)
    ax.errorbar(x=N, y=mean, yerr=sem,
                fmt='o', capsize=5, label='Simulation')
    ax.set(
        xlabel='Population size (N)',
        ylabel='Fixation time',
        xscale='log',
        xlim=(0.5 * Nrange.min(), 1.5 * Nrange.max()),
    )
    return fig, ax
fixation_time_plot(Nrange, fix_time_sim[:,0], fix_time_sim[:,1]);
plt.show()
fig.savefig("part2_Dotplot.png")