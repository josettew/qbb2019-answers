#!/usr/bin/env python3

import sys

f = open(sys.argv[1])  
for i, line in enumerate(f):
    columns = line.split( ) # split columns by whitespace
    for field in columns:   # for the fields in the column
        if field.endswith("DROME"):     #if the field ends with DROME then...
            if "FBgn" not in columns[-1]: #remove any gene names that do not start with FBgn
                continue
            print(columns[-1], columns[-2]) #print the last and second to last columns
             # save stdout to fly_id_columns.txt using >
   
 