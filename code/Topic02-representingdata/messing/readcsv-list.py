# A program to read in the iris data set from a CSV file
# Author: Andrew Beatty

import csv
FILENAME = "iris.csv"
DATA_FOLDER = "../iris-datafiles/"

with open (DATA_FOLDER + FILENAME, "rt") as irisfile:
    # as lists
    irisreader = csv.reader(irisfile, delimiter=',',quoting = csv.QUOTE_NONE)
    linecount = 0
    alldata = []
    for line in irisreader:
        #if not linecount: # header row
        print (line)
        #    print ("--------------------------------------") 
        #else: # not the header row   
            #print(line)
            #line.append (line[0] * line[1])
            alldata.append(line)

        #linecount += 1
    print (alldata)