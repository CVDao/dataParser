#find all .txt/word doc files in folder
import os, glob
import numpy as np
filetype = "*.txt"

targs = glob.glob(filetype)

# processes the files of extraneous data

for i in targs:
    f = open(i, "r")
    lines = f.readlines()
    f.close()

    temp = i[0: len(i)-3] + "t"
    f = open(temp, "w")
    for line in lines:
        if not ">>>>>" in line:
            f.write(line)
    f.close()
#
targs = glob.glob("*.t")

tempDict = {}
tArray = np.loadtxt(targs[0], dtype = float)
for i in tArray:
    tempDict[i[0]] = [i[1]]

for i in range(1, len(targs)):
    tArray = np.loadtxt(targs[i], dtype = float)
    for i in tArray:
        tempDict[i[0]].append(i[1])

print(tempDict)
