#!/usr/bin/env python3

import sys
# arugment is SRR072893.SAM
if len(sys.argv)>1: 
    f = open(sys.argv[1]) #if you have an arugment with atleast 1 character, open the file
else:
    f = sys.stdin #otherwise set f = <, take previous output and pipe into the command

for i, line in enumerate(f,1): 
    if line.startswith("@"):
        continue
    fields = line.split("\t")
    if fields[2] == "*":
        i += -1
        continue
    elif i>10:
        break
    else:
        print(fields[2])