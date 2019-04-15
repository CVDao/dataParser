#find all .txt/word doc files in folder
import os, glob
import numpy as np
import pandas as pd
import xlsxwriter as xwriter


#Settings
filetype = "*.txt"
targs = glob.glob(filetype)

# processes the files of extraneous data

for i in targs:                     #for every file
    f = open(i, "r")                #open it in a read only state
    lines = f.readlines()           #read the lines and store
    f.close()

    temp = i[0: len(i)-3] + "t"     #The output file removes .txt and appends .t 
    f = open(temp, "w")             #the temp files are the original file, minus the metadata

    start = 0
    for line in range(len(lines)):
        if ">>>>>" in lines[line]:
            start = line + 1
            break

    for line in (range(start, len(lines))):
        if ">>>>>" in lines[line]:
            break

        f.write(lines[line])

    f.close()
#
targs = glob.glob("*.t") # look over all the temp files made

tArray = np.loadtxt(targs[0], dtype = float) #have numpy process them
tArray = tArray.tolist() # turn the first input into a list

#sort all the data points into their slots
for i in range(1, len(targs)):
    t2Array = np.loadtxt(targs[i], dtype = float).tolist()
    for i in range(len(t2Array)):
        tArray[i].append(t2Array[i][1])
a = ["Wave Length"]
for i in range(len(tArray[0])-1):
    a.append(i)
tArray = [a] + tArray

workbook = xwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()

for row, data in enumerate(tArray):
    worksheet.write_row(row, 0, data)
workbook.close()
