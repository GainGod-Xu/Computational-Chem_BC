#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os,math,sys
#
def greadSI(filename):
    ifs = open(filename, 'r')
    while 1:
          line=ifs.readline()
          if not line: break
          data=line.split()

#########################Read xyz Coordinates#################################
          if len(data)>0: # if true, line is not blank
             if data[0]=='Standard':
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
                  ### create a format for your atom information by using a list and store into frame.
                      atominfo=[atomid,atomtype,atomx,atomy,atomz]
                      frame.append(atominfo)

                      line=ifs.readline()
                      data=line.split()
 
##############################Reading Thermal data#########################
          if len(data)>4: # if true, line is not blank
             if data[0]=='Temperature':
                P= float(data[4])
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

          if len(data)>=1: # if true, line is not blank
             if data[0]=='1':
                line=ifs.readline() # contains "A                      A                      A" 
                data=line.split()
                if len(data)>=1:
                   if data[0]=='A' or data[0]=='SGG':
                      line=ifs.readline() # contains "Frequencies --"
                      data=line.split()
                      freq=float(data[2])
 
#########################################################
    ofs_name=filename[:-4]+'_SI.txt'
    ofs = open(ofs_name,'w')

    print('Thermal Data is writing on there!')
      
    ofs.write('Temperature: ' + str(T) + ' Kelvin'+ '\n')
    ofs.write('Pressure: ' + str(P) + ' Atm' + '\n')
    if freq < 0:
       ofs.write('Imaginary Frequency: ' + str(freq) + ' cm-1 ' + '\n')
       
    SCF=G_sum-G_corr
    ofs.write('G_corr: '+ str(G_corr) + ' Hartree'+'\n')
    ofs.write('H_corr: '+ str(H_corr) + ' Hartree'+'\n')
    ofs.write('SCF: '+ str(SCF) + ' Hartree'+'\n')
    ofs.write('S: '+ str(S_tot) + ' Cal/Mol-Kelvin'+'\n')
    ofs.write('H: '+ str(H_sum) + ' Hartree'+'\n')
    ofs.write('G: '+ str(G_sum) + ' Hartree'+'\n')

    print('xyz coordination is writing on there!')
    ofs.write('\n')
    ofs.write('Cartesian Coordinates:' + '\n')
    #ofs.write(str(len(frame)) + '\n\n')
    for i in frame:
        ofs.write('%2s' % str(i[1]) + ' ' +  '%12.8f' % float(i[2]) + ' ' + '%12.8f' % float(i[3]) + ' ' + '%12.8f' % float(i[4]) + '\n')

    ofs.write('\n\n')
    ifs.close()
    ofs.close()
    print('Congrats on there on there!!!\n\n')
    print('**************************************\n')
    print( ofs_name + ' is your output!\n\n')

if __name__ == "__main__":
   filename= sys.argv[1]
   greadSI(filename)


