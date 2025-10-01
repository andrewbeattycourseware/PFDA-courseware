# case study of iris data set
# area of sepia and petals
# Author Andrew Beatty

import csv

FILENAME= "irisquotes.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    
    for line in reader:
        sepal_size= line['sepal_length'] * line['sepal_width']
        petal_size= line['petal_length'] * line['petal_width']
        line["sepal_area"] = sepal_size
        line["petal_area"] = petal_size
        
        print (line)
        