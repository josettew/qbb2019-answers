#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import seaborn as sns

# argv1=fimo.tsv

f = open(sys.argv[1])

locations = []

for line in f:
    if line.startswith("motif_id"):
        continue
    col = line.rstrip("\n").split()
    if col != []:
        locations.append(int(col[3]))

    
    
fig, ax = plt.subplots()    
ax = sns.distplot(a=locations, bins = 10)

fig.savefig("densityplot.png")
plt.close(fig)