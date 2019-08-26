#!/usr/bin/env python3

import sys
# arugment is SRR072893.SAM
if len(sys.argv)>1: 
    f = open(sys.argv[1]) #if you have an arugment with atleast 1 character, open the file
else:
    f = sys.stdin #otherwise set f = <, take previous output and pipe into the command
count = 0
for line in f:
    fields = line.split("\t")
    for field in fields:
        if field == "NM:i:0":
            count += 1 
print(count)