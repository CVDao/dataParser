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

tArray = np.loadtxt(targs[0], dtype = float)
tArray = tArray.tolist()

for i in range(1, len(targs)):
    t2Array = np.loadtxt(targs[i], dtype = float).tolist()
    for i in range(len(t2Array)):
        tArray[i].append(t2Array[i][1])
a = ["Wave Length"]
for i in range(len(tArray[0])-1):
    a.append(i)
tArray = [a] + tArray
print(tArray)
