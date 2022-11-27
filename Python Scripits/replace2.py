#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os
 
import re
 
#list files
 
def listFiles(dirPath):
 
    fileList=[]
 
    for root,dirs,files in os.walk(dirPath):
 
        for fileObj in files:
 
            fileList.append(os.path.join(root,fileObj))
 
    return fileList
 
  
 
def main():
 
    fileDir = "./"
 
    regex = ur'FUNC_SYS_ADD_ACCDETAIL'
 
    fileList = listFiles(fileDir)
 
    for fileObj in fileList:
  
        name = fileObj
        if name.endswith(".gjf"):
            print name
            f = open(fileObj,'r+')
 
            all_the_lines=f.readlines()
 
            f.seek(0)
 
            f.truncate()
             
 
            for line in all_the_lines:
#                orig_line1 = "# opt=modredundant gen bp86 fopt=(modredundant,maxcycle=15)"
#                replace_line1 = "#  bp86/gen sp" 
#                f.write(line.replace(orig_line1,replace_line1))   
                orig_line2 = "B 6 60 S 40 0.050000"
                replace_line2 = "C N S O H 0\n6-311G*\n****\nCo 0\ndef2svp\n****\n"
                f.write(line.replace(orig_line2,replace_line2))
#                orig_line3 = "%mem=32GB"
#                replace_line3 = " "
#                f.write(line.replace(orig_line3,replace_line3))
#                orig_line4 = "ed=28"
#                replace_line4 = "%mem=32GB"
#                f.write(line.replace(orig_line4,replace_line4))
 
            f.close() 
 
if __name__=='__main__':
 
    main()


