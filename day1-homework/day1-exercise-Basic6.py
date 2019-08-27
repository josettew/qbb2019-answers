#!/usr/bin/env python3

import sys
# arugment is SRR072893.SAM
if len(sys.argv)>1: 
    f = open(sys.argv[1]) #if you have an arugment with atleast 1 character, open the file
else:
    f = sys.stdin #otherwise set f = <, take previous output and pipe into the command
count = 0 #starting point
for i, line in enumerate(f): 
    if line.startswith("@"):
        continue
    fields = line.split("\t")
    if fields[2] == "*":
        continue
    if int(fields[3]) >= 10000 and int(fields[3]) <=20000 and fields[2] == "2L":
        count +=1 #add 1 for each line, starting at 0
print(count)