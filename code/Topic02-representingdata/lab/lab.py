import csv
DATADIR = "./"
FILENAME="data.csv"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        print (line)
        if not linecount: # first row ie header row
            pass
        else: # all subsequent rows
            total += int(line[1]) # why 1
            print (line[1])
        linecount += 1
print (f"average is {total/(linecount-1)}") # why -1 ?
