#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

allele_frequency = []
for line in open(sys.argv[1]):
   if line.startswith("#"):
       continue
   field = line.rstrip("\n").split()
   info = field[7]
   allele_frequency_split = info.split("=")[1]
   allele_frequency_split = allele_frequency_split.split(",")
   for number in allele_frequency_split:
       allele_frequency.append(float(number))

fig, ax = plt.subplots()
plt.hist(allele_frequency,bins = 100)
plt.xlabel("allele")
plt.ylabel("frequency")
plt.title("Allele Frequency")
fig.savefig("allelefreq.png")
plt.close(fig)