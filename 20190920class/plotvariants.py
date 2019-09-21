#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt


dp = []
qual_score = []
af = []
ann_dict = {}

for line in open(sys.argv[1]):
   if line.startswith("#"):
       continue
   col = line.rstrip("\n").split("\t")
   ref = col[3]
   alt = col[4]
   qual = int(float(col[5]))
   info = col[7]
   dp_split = info.split(";")[7]
   dp.append(dp_split.split("=")[1])
   qual_score.append(qual)
   
   af_split = info.split(";")[3]
   af.append(af_split.split("=")[1])
   
   ann_split = info.split(";")[41]
   ann_value = ann_split.split("=")[1]
   ann_score = ann_value.split("|")[1]
   if ann_score in ann_dict:
         ann_dict[ann_score] += 1
   else:
         ann_dict[ann_score] = 1
       
   
  
   
   
fig, ax = plt.subplots(4)
ax[0].hist( dp, bins=100)
ax[1].hist( qual_score, bins=1000, range=[0,5000])
ax[2].hist( af, bins=100 )
plt.bar(range(len(ann_dict)), list(ann_dict.values()), align = 'center')
plt.xticks(range(len(ann_dict)), list(ann_dict.keys()), rotation = 'vertical', size = 5)

ax[0].set_xlabel("Variants")
ax[0].set_ylabel("Read Depth")

ax[1].set_xlabel("Variants")
ax[1].set_ylabel("Quality")

ax[2].set_xlabel("Variants")
ax[2].set_ylabel("Frequency")

ax[3].set_xlabel("Impact")
ax[3].set_ylabel("Frequency")

ax[0].set_title("Graph1-Read Depth")
ax[1].set_title("Graph2-Quality")
ax[2].set_title("Graph3-Allele Frequency")
ax[3].set_title("Graph4-Impact")

fig.savefig( "results.png" )
plt.close(fig)