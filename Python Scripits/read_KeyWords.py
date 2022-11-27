#!/usr/bin/python
import os,time,re,string

# Keywords for your desired content(data) searching
keywords = str(input("please input your keywords with \"  \" \n"))

# File Type for reading files
f1_type = str(input("please input your file type with \"  \" \n"))

# Name your outfile
#output_name = str(input("please input your output name \"  \"\n"))

data = []
simple_data =[]
# the path of your txt files
fileList=os.listdir('./')

# make the order of all files
fileList.sort()

print("**************************************\n")

# select your txt file and read specific content you wanted
for file in fileList:
    print(file)	
    if file.endswith(f1_type):
       f1 = open(file, "r") 
       for line in f1.readlines():
           if keywords in line:
              data.append(file + ':  ')
              data.append(line + '\n')
              simple_data.append(line)

       f1.close()
       print(file + " was read!")
print("**************************************\n")
print("Going to write your data into a new file!\n")
print("**************************************\n")
             
# Write content(data) to output file.
f2 = open('./reading.output', 'w')
for data_line in data:
    f2.write(str(data_line))
f2.close()


f3 = open('./reading_simple.output', 'w')
for data_line in simple_data:
    f3.write(str(data_line))
f3.close()

print("*****************************************************************************************\n")
print("Amazing! Well Done. Please find your output!\n\n")
print("Your data is sucessfully stored into ***reading.output*** in current folder!\n\n")
print("Your data is sucessfully stored into ***reading_simple.output*** in current folder!\n\n")
print("*****************************************************************************************\n")


