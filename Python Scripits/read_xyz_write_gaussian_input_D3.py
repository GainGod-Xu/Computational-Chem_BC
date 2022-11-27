#!/usr/bin/python
import shutil,os,math,sys

### the following two lines read your .xyz file and store its name 
ifs_name= sys.argv[1]

ofs_name=ifs_name[:-4]+'_D3.com'
chk_name=ifs_name[:-4]+'_D3.chk'
 
### open your xyz file 
ifs = open(ifs_name, 'r')

### create a list for coordinates, then read all lines(atom and xyz) into this list
xyz_cor=[]
for line in ifs.readlines()[2:]:
    xyz_cor.append(line)

ifs.close()

    
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
ofs.write('#p b3lyp/gen sp EmpiricalDispersion=GD3BJ \n')

ofs.write('\n')

### write your comment line
ofs.write('comment  \n')

ofs.write('\n')

### write your charge and multiplicity
ofs.write('0 2 \n')

### write all lines from your list into com file.
for line in xyz_cor:
    ofs.write(str(line))


### write an space line
ofs.write('\n')

### your gen basis set
ofs.write('C N Cl Na O H 0\n')
ofs.write('def2tzvp\n')
ofs.write('****\n')
ofs.write('Co 0\n')
ofs.write('def2tzvp\n')
ofs.write('****\n')

### write an space line
ofs.write('\n')


ofs.close()
