#!/usr/bin/env python3

"""
Usage: ./01-hist.py <ctab>
Plot FPKMs
"""
## run this:  ./01-histogram.py ../results/stringtie/SRR072893/t_data.ctab 

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pandas as pd



ctab = pd.read_csv(sys.argv[1], sep = "\t")
goi = ctab.loc[:, "FPKM"] > 0 
#graph a log transformed version of data
my_data = np.log2(ctab.loc[goi, "FPKM"])

fig, ax = plt.subplots()

a = float(sys.argv[2])
loc = float(sys.argv[3])
scale = float(sys.argv[4])
loc_norm = float(sys.argv[5])
scale_norm = float(sys.argv[6])
x = np.linspace(-15, 15, 100)
y = stats.skewnorm.pdf(x, a, loc, scale)

y_norm = stats.norm.pdf(x, loc_norm, scale_norm)
ax.plot(x, y_norm)

ax.hist(my_data, bins = 100, density = True)
#add bell curve line to plot
ax.plot(x,y,color="green")
ax.set_title("Histogram For Lunch Exercise 1")
ax.set_xlabel("log2 of fpkms")
ax.set_ylabel("% of frequency")
plt.text(-8, 0.15, 'a = %s\nloc = %s\nscale = %s'% (str(a), str(loc), str(scale)))
fig.savefig("fpkms.png")
plt.close(fig)