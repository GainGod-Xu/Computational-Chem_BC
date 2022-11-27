#!/usr/bin/python
import os,math,sys
#


## program reads gaussian log file. looks for line with checkpoint file. writes com file. uses HF method. does not matter.  and submits
filename= sys.argv[1]
ifs = open(filename, 'r')

file_extension=filename[-3:]

#T= sys.argv[2]

com=filename[:-4] +'_' + str(313.15) + '.com' 

ofs = open(com, 'w')

while 1:
      line=ifs.readline()
      if not line: break
      data=line.split()
      if len(data)>0: # if true, line is not blank
         if '%chk=' in data[0]:
            chk= data[0]  # skip header lines

         if data[0]=='Charge' and data[3]=='Multiplicity': 
            charge=data[2]
            mult=data[5]

ofs.write('%mem=20gb' + '\n')
ofs.write('%nprocshared=8' + '\n')

ofs.write(chk + '\n')
ofs.write('# HF' + ' geom=check guess=check freq=readfc  ' + 'temperature=' +str(313.15)  + '\n') 
ofs.write('\n')
ofs.write('comment  \n')
ofs.write('\n')
txt=str(charge) + ' ' + str(mult) + '\n'
ofs.write(txt)
ofs.write('\n\n') 
         
ofs.close()
