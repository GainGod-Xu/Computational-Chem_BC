#!/usr/bin/python
import os,time

fileList=os.listdir('./')

# make the order of all files
fileList.sort()

for file in fileList:
    if file.endswith(".chk"):
       print("formchk " + file)
       time.sleep(0.05)

