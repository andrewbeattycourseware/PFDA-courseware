# A program to read in the iris data set from a CSV file
# Author: Andrew Beatty

import csv
FILENAME = "irisfloats.csv"
DATA_FOLDER = "../iris-datafiles/"

with open (DATA_FOLDER + FILENAME, "rt") as irisfile:
    # as lists
    irisreader = csv.DictReader(irisfile, delimiter=',')
    for line in irisreader:
        print (line)