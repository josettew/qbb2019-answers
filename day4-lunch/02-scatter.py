#!/usr/bin/env python3

"""
Usage: ./00-scatter.py <ctab>
Compare num_exons vs length
"""
## run this:  ./02-scatter.py ../results/stringtie/SRR072893/t_data.ctab ../results/stringtie/SRR72894/t_data.ctab

import sys
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np


fpkm1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name")

fpkm2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = "t_name")

data1 = np.log2(ctab1.loc[:, "FPKM"] + 0.01)
data2 = np.log2(ctab2.loc[:, "FPKM"] + 0.01)

m,b = np.polyfit(data1, data2, 1)
x = np.linspace(data1.min(), data1.max(), 2)

fig, ax = plt.subplots()
# cant assume x and y values so must define them
# x then y axis
ax.scatter( x=data1, y=data2, s = 3, alpha = .3)
ax.plot(x, [(m*x1)+b for x1 in x], color = "red", label = 'y = %sx + %s' %(str(m)[:5], str(b)[:5]))
# choosing where to place a line on the graph (x-coordinates) (y-coordinates)
#ax.plot([0,40], [0,20000], color = "red")
ax.set_title("Lunch Exercise 2")
ax.set_xlabel("log2 FPKMs SRR072893")
ax.set_ylabel("log2 FPKMs SRR072894")
ax.legend(loc = 'upper left', fontsize = 8)
fig.savefig("fpkms_scatter.png")
plt.close(fig)
