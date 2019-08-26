#!/usr/bin/env python3

import sys
# arugment is SRR072893.SAM
if len(sys.argv)>1: 
    f = open(sys.argv[1]) #if you have an arugment with atleast 1 character, open the file
else:
    f = sys.stdin #otherwise set f = <, take previous output and pipe into the command

mapq = []
for line in f:
    if line.startswith("@"):
            continue
    fields = line.split("\t")
    if fields[2] == "*":
        continue
    mapq.append(int(fields[4]))

summap = sum(mapq)
length = len(mapq)

average = summap / length
print(average)
