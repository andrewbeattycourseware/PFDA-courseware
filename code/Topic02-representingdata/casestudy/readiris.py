# case study of iris data set
# area of sepia and petals
# Author Andrew Beatty

import csv

FILENAME= "iris.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_NONE)
    
    for line in reader:
        sepal_size= float(line[0]) * float(line[1])
        petal_size= float(line[2]) * float(line[3])
        line.append(sepal_size)
        line.append(petal_size)
        print (line)
        