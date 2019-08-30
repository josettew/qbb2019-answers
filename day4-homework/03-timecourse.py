#!/usr/bin/env python3

"""
Usage: ./02-timecourse.py <t_name> <samples.csv> <FPKMs>
create a timecourse of a given transcript for females
"""
## input: ./03-timecourse.py FBtr0331261 ~/qbb2019/data/samples.csv all.csv 

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


t_name = sys.argv[1]
samples = pd.read_csv(sys.argv[2])

def sex_sorter(sex):
   soi = samples.loc[:,"sex"] == sex
   stages = samples.loc[soi,"stage"]
   # print(srr_ids)

   #load fpkms
   fpkms = pd.read_csv(sys.argv[3],index_col="t_name")

   #extract data
   my_data =[]
   for stage in stages:
       # print(srr_id)
       my_data.append(fpkms.loc[t_name,sex + '_' + stage])
   return my_data

male_data = sex_sorter("male")
female_data = sex_sorter("female")
#male_data_last4 = male_data[4:8]
#female_data_last4 = female_data[4:8]
labelz = ["male", "female"]
label2 = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]

# print(my_data)

fig,ax = plt.subplots()
ax.plot(male_data, color="blue")
#ax.plot(male_data_last4, color="green")
ax.plot(female_data, color="red")
#ax.plot(female_data_last4, color="orange")
ax.set_title("Homework Exercise 3 Sxl Males and Females")
ax.set_xlabel("devlopmental stage")
ax.set_xticklabels(label2, rotation = "vertical")
ax.set_xticks(np.arange(len(label2)))

ax.set_ylabel("mRNA abundance (RPKM)")
plt.legend( labels = labelz, loc='center left', bbox_to_anchor=(1, .5))
plt.tight_layout()
fig.savefig("timecourse.png")
plt.close(fig)