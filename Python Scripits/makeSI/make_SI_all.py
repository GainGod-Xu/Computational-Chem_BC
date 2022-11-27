#!/usr/bin/python
import os,time,re,string

from prep_SI_main import greadSI

# File Type for reading files
f1_type = str(input("please input your file type with \"  \" \n"))

# the path of your txt files
fileList=os.listdir('./')

# make the order of all files
fileList.sort()

print("********************************************\n")

# select your txt file and read specific content you wanted
for file in fileList:
    if file.endswith(f1_type):
       print('Data is extracted from ' + file ) 
       greadSI(file)
       print("********************************************\n")

data=[]
# File Type for reading files
f2_type = str(input("please input your file type with \"  \" \n"))

# the path of your txt files
fileList=os.listdir('./')
fileList.sort()
for file in fileList:
    if file.endswith(f2_type):
       f2 = open(file, "r")
       data.append('---------------------------------------------------------------------'+'\n')
       data.append(file + ' ' + '\n\n')
       for line in f2.readlines():
           data.append(line)
       f2.close()
       print(file + " was read!")
print("**************************************\n")
print("Going to write your data into a new file!\n")
print("**************************************\n")
             
# Write content(data) to output file.
f3 = open('./00_all_SI.output', 'a')
for data_line in data:
    f3.write(str(data_line))
f3.close()

 
                
print("*****************************************************************************************\n")
print("Amazing! Well Done. Please find your output!\n")
print("*****************************************************************************************\n")


