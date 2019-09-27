#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

components = open(sys.argv[1])

fam_set = set()
all_data = []
fam_colors = {}


for line in components:
    col = line.rstrip('\n').split(' ')
    family = (col[0])
    x = float(col[2])
    y = float(col[3])
    all_data.append((family, x, y))
    fam_set.add(family)
    
colors = ['#800000' ,'#9A6324', '#e6194B', '#808000', '#ffe119', '#469990', '#000075', '#000000', '#f032e6', '#aaffc3', '#a9a9a9']
fam_set = list(fam_set)

for i in range(len(fam_set)):
    fam_colors[fam_set[i]] = colors[i]
    
fig, ax = plt.subplots()
for point in all_data:
    ax.scatter(point[1], point[2], color = fam_colors[point[0]])

plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.title("Principal Component Analysis")
fig.savefig ("pca.png")
plt.close(fig)

    