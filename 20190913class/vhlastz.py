#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt

f = open(sys.argv[1])
list_x =[]
list_y = []
for i, line in enumerate(f):
    if i == 0:
        continue
    col = line.rstrip('\n').split('\t')
    start = col[4]
    end = col[5]
    contig = col[8]
    y = (int(end)) - (int(start))
    list_x.append(int(col[8]))
    list_y.append(y)

fig, ax = plt.subplots()
fig.suptitle("MAP006 Dotplot")

ax.scatter(list_x,list_y, alpha = 0.2)
ax.set_xlabel("Len of Ref")
ax.set_ylabel("Len of Contig")

fig.savefig("MAPdotplot")
plt.close(fig)