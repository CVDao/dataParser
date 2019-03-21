#find all .txt/word doc files in folder
import os, glob
filetype = "*.txt"

targs = glob.glob(filetype)

# compiles them into an exel doc
