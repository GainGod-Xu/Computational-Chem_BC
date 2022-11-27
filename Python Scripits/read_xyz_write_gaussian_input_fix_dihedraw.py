#!/usr/bin/python
import os,math,sys

### the following two lines read your .xyz file and store its name 
ifs_name= sys.argv[1]
ifs = open(ifs_name,'r')
ofs_name=ifs_name[:-4]+'_ropt.com'
chk_name=ifs_name[:-4]+'_ropt.chk'
 
xyz=[]
for line in ifs.readlines()[2:]:
    xyz.append(line)

    
### create and open new com file.
ofs=open(ofs_name,'w')

### write all informations into your com file.
### how many gb for memmory?
ofs.write('%mem=120gb \n')

### how many cores?
ofs.write('%nprocshared=28 \n')

### write your the name of your chk file 
ofs.write('%chk=' + chk_name + '\n')

### write functional, basis set and keywords
ofs.write('#p bp86/gen  opt=modredundant \n')

ofs.write('\n')

### write your comment line
ofs.write('comment  \n')

ofs.write('\n')

### write your charge and multiplicity
ofs.write('0 2 \n')

### write xyz
for line in xyz:
    ofs.write(str(line))

### write an space line
ofs.write('\n')

### fixed dihedraw###

ofs.write('D 3 1 2 18 F\n')

### write an space line
ofs.write('\n')

### your gen basis set
ofs.write('C N S O H 0\n')
ofs.write('6-311G*\n')
ofs.write('****\n')
ofs.write('Co 0\n')
ofs.write('def2svp\n')
ofs.write('****\n')

### write an space line
ofs.write('\n')

ifs.close()
ofs.close()
