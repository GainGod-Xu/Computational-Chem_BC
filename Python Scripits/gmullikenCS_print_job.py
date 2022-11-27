#!/usr/bin/python
import os,time

# read all the file names into fileList.
fileList=os.listdir('./')

# make the order of all files
fileList.sort()

for file in fileList:
    if file.endswith(".log"):
       print("gmullikenCS " + file + "| grep N| grep 6")
       time.sleep(0.05)
