#!/usr/bin/python
import os,math,sys
##
jobtype = str(input("please input your job type(TS? opt? freq?) with \"  \" \n"))
mem = str(input("please input your memory: only number) with \"  \" \n"))
np = str(input("please input your core: only number) with \"  \" \n"))

ifs_name= sys.argv[1]
ifs = open(ifs_name, 'r')


xyz_cor=[]

for line in ifs.readlines()[2:]:
    xyz_cor.append(line)
ifs.close()

if jobtype == 'TS':
   ofs_name=ifs_name[:-4]+'_TS.com'
   chk_name=ifs_name[:-4]+'_TS.chk'

elif jobtype == 'opt':
   ofs_name=ifs_name[:-4]+'_opt.com'
   chk_name=ifs_name[:-4]+'_opt.chk'

elif jobtype == 'freq':
   ofs_name=ifs_name[:-4]+'_freq.com'
   chk_name=ifs_name[:-4]+'_freq.chk'

else:
   pass
 

ofs=open(ofs_name,'w')
ofs.write('%mem=' + mem + 'GB \n')
ofs.write('%nprocshared=' + np + '\n')
ofs.write('%chk=' + chk_name + '\n')

if jobtype == 'TS':
   ofs.write('#bp86/def2svp opt=(calcfc,ts,noeigentest) \n')

elif jobtype == 'opt':
   ofs.write('#bp86/def2svp opt \n')

elif jobtype == 'freq':
   ofs.write('#bp86/def2svp freq \n')
 
else:
   pass

ofs.write('\n')
ofs.write('comment  \n')
ofs.write('\n')
ofs.write('0 2 \n')
for line in xyz_cor:
    ofs.write(str(line))
ofs.write('\n')
ofs.write('\n')
ofs.write('\n')
ofs.close()
