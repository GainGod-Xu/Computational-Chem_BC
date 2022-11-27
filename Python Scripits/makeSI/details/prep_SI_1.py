#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os,math,sys
#
filename= sys.argv[1]
ofs_name=filename[:-4]+'_SI.txt'
ofs = open(ofs_name,'w')
ifs = open(filename, 'r')
print('Data is extracted from ' + filename)

while 1:
      line=ifs.readline()
      if not line: break
      data=line.split()
      if len(data)>0: # if true, line is not blank
         if data[0]=='Input' or data[0]=='Standard' or data[0]=='Z-Matrix':
            if data[1]=='orientation:': # Found Standard Orientation
              frame=[]
              line=ifs.readline()  # skip header lines
              line=ifs.readline()  # skip header lines
              line=ifs.readline()  # skip header lines
              line=ifs.readline()  # skip header lines
              line=ifs.readline()  # first line containing atom info
              data=line.split()
              while data[0]<>'---------------------------------------------------------------------':
                  
                  atomid=data[0]
                  if   data[1]=='1':   atomtype='H'
                  elif data[1]=='2':   atomtype='He'
                  elif data[1]=='10':   atomtype='Ne'
                  elif data[1]=='18':   atomtype='Ar'
                  elif data[1]=='6':   atomtype='C'
                  elif data[1]=='8':   atomtype='O'
                  elif data[1]=='7':   atomtype='N'
                  elif data[1]=='17':  atomtype='Cl'
                  elif data[1]=='9':   atomtype='F' 
                  elif data[1]=='14':  atomtype='Si' 
                  elif data[1]=='16':  atomtype='S'
                  elif data[1]=='5' :  atomtype='B'
                  elif data[1]=='15' : atomtype='P'
                  elif data[1]=='35' : atomtype='Br'
                  elif data[1]=='29' : atomtype='Cu'
                  elif data[1]=='44' : atomtype='Ru'
                  elif data[1]=='53' : atomtype='I'
                  elif data[1]=='3' : atomtype='Li'
                  elif data[1]=='42' : atomtype='Mo' 
                  elif data[1]=='30' : atomtype='Zn'
                  elif data[1]=='13' : atomtype='Al'
                  elif data[1]=='11' : atomtype='Na'
                  elif data[1]=='19' : atomtype='K'
                  elif data[1]=='74' : atomtype='W'
                  elif data[1]=='47' : atomtype='Ag'
                  elif data[1]=='26' : atomtype='Fe'
                  elif data[1]=='45' : atomtype='Rh'
                  elif data[1]=='46' : atomtype='Pd'
                  elif data[1]=='78' : atomtype='Pt'
                  elif data[1]=='77' : atomtype='Ir'
                  elif data[1]=='27' : atomtype='Co'
                  elif data[1]=='37' : atomtype='Rb'
                  elif data[1]=='40' : atomtype='Zr'
                  elif data[1]=='28' : atomtype='Ni'
                  elif data[1]=='55' : atomtype='Cs'
                  elif data[1]=='34' : atomtype='Se'
                  elif data[1]=='12' : atomtype='Mg'
                  else: 
                      print data,'no atom type found, exiting....'
                      exit
                  
                  if len(data)==6: 
                     atomx=data[3]
                     atomy=data[4]
                     atomz=data[5]
                  elif len(data)==5:
                     atomx=data[2]
                     atomy=data[3]
                     atomz=data[4] 
                  else: 
                     print 'cannot work out Standard orientation format. exiting..'
                     break 
                  ### create a format for your atom information by using a list
                  atominfo=[atomid,atomtype,atomx,atomy,atomz]
                  #print atominfo   
                  ### store your atom information into frame
                  frame.append(atominfo)
                  ##read  
                  line=ifs.readline()
                  data=line.split()
############reading Thermal data#########################

      if len(data)>4: # if true, line is not blank
         if data[0]=='Temperature':
            ofs.write('Temperature:' + data[1] + ' ' + data[2] + '\n')
            ofs.write('Pressure:' + data[4] + ' ' + data[5] + '\n')

            T=float(data[1])
         if data[0]=='Sum' and data[2]=='electronic' and data[5]=='Enthalpies=': H_sum=float(data[6])
         if data[0]=='Sum' and data[2]=='electronic' and data[5]=='Free': G_sum=float(data[7])
         if data[0]=='Thermal' and data[1]=='correction' and data[3]=='Gibbs': G_corr=float(data[6])
         if data[0]=='Thermal' and data[1]=='correction' and data[3]=='Enthalpy=': H_corr=float(data[4])
         if data[0]=='Cartesian' and data[1]=='Forces:':
            F_max=float(data[3])
            F_rms=float(data[5])
         if data[0]=='Zero-point' and data[1]=='correction=': ZPE_corr=float(data[2])

      if len(data)>2: # if true, line is not blank
         if data[0]=='KCal/Mol' and data[1]=='Cal/Mol-Kelvin':
            line=ifs.readline() # line contains 'Total' E, CV, and S
            data=line.split()
            S_tot=float(data[3])
            line=ifs.readline() # contains "ELectronic" 
            line=ifs.readline() # contains "Translational"
            data=line.split()
            S_trans=float(data[3])
            line=ifs.readline() # contains "Rotational"
            data=line.split()
            S_rot=float(data[3])
            line=ifs.readline() # contains "Vibrational"
            data=line.split()
            S_vib=float(data[3])

      if len(data)>2: # if true, line is not blank
         if data[0]=='1' and data[1]=='2' and data[2]=='3':
            line=ifs.readline() # contains "A                      A                      A" 
            data=line.split()
            if len(data)>2:
               if data[0]=='A' and data[1]=='A' and data[2]=='A':

                  line=ifs.readline() # contains "Frequencies --"
                  data=line.split()
                  freqs=[]
                  freqs.append(data[2])
                  freqs.append(data[3])
                  freqs.append(data[4])


####Thermal Data####
print('Thermal Data is writing on there!')
SCF=G_sum-G_corr
#print 'G_sum', G_sum
#print 'G_corr', G_corr
#print 'H_corr', H_corr 
#print 'SCF', SCF
#print 'S_tot', S_tot
#print 'S_trans', S_trans
#print 'S_rot', S_rot
#print 'S_vib', S_vib

if float(freqs[0]) < 0:
   ofs.write('Frequencies: ' + str(freqs[0]) + ' cm-1 ' + '\n')

ofs.write('G_corr: '+ str(G_corr) + ' Hartree'+'\n')
ofs.write('H_corr: '+ str(H_corr) + ' Hartree'+'\n')
ofs.write('SCF: '+ str(SCF) + ' Hartree'+'\n')
ofs.write('S: '+ str(S_tot) + ' Hartree'+'\n')
ofs.write('H: '+ str(H_sum) + ' Hartree'+'\n')
ofs.write('G: '+ str(G_sum) + ' Hartree'+'\n')

#print 'G using 50% of S_trans', SCF+H_corr-T*(0.5*S_trans+S_rot+S_vib)/627.51/1000.0


###########xyz coordination###
print('xyz coordination is writing on there!')
ofs.write('\n')
ofs.write('Cartesian Coordinates:' + '\n')
#ofs.write(str(len(frame)) + '\n\n')
for i in frame:
    ofs.write(i[1] + ' ' +  '%7.3f' % float(i[2]) + ' ' + '%7.3f' % float(i[3]) + ' ' + '%7.3f' % float(i[4]) + '\n')

ofs.write('\n\n')
ifs.close()
ofs.close()

print('Congrats on there! It is finished! So beatiful on there!!!')
