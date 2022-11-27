#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os,math,sys
#

def ext_HL(input_file):
    ifs = open(input_file, 'r')
    alpha_LUMO=0
    beta_LUMO=0
    
    ### read obitals###
    for line in ifs.readlines():
        data=line.split()
        if len(data)>4: # if true, line is not blank
           if data[0]=='Alpha' and data[1] == 'occ.':
              alpha_HOMO=float(data[(len(data)-1)])
           elif data[0]=='Alpha' and data[1] == 'virt.':
              if not alpha_LUMO:
                 alpha_LUMO=float(data[4])
              else:
                 continue
           elif data[0]=='Beta' and data[1] == 'occ.':
              beta_HOMO=float(data[(len(data)-1)])
           elif data[0]=='Beta' and data[1] == 'virt.':
              if not beta_LUMO:
                 beta_LUMO=float(data[4])
              else:
                 continue
    return alpha_HOMO,alpha_LUMO,beta_HOMO,beta_LUMO
    ifs.close()

###Global Electrophilicity Index: gEI ###
def calc_gEI(alpha_HOMO,alpha_LUMO,beta_HOMO,beta_LUMO):
    ###Global Chemical Potential: gCP ###
    gCP = (alpha_HOMO + beta_LUMO)/2
    
    ###Global Chemical Hardness: gCH ###
    gCH = (beta_LUMO - alpha_HOMO)

    gEI= gCP*gCP/(2*gCH)*27.2114
    
    return gEI,gCP,gCH

def calc_lEI(gEI,gCP,gCH,input_file):
    CS_file= input_file[:-4]+'.CS'
    ifs = open(CS_file, 'r')
    ###The local radical Parr function###
    for line in ifs.readlines():
        data=line.split()
        if float(data[3]) > 0.5:
           ASD = float(data[3])
           break
        elif float(data[3]) < -0.5:
           ASD = float(data[3])
           break
    lEI = ASD*gEI
    lCP = ASD*gCP
    lCH = ASD*gCH
    return lEI,lCP,lCH,ASD            

if __name__ == "__main__":
   input_file = sys.argv[1] # It is your spe .log file
   alpha_HOMO,alpha_LUMO,beta_HOMO,beta_LUMO = ext_HL(input_file)
   gEI,gCP,gCH = calc_gEI(alpha_HOMO,alpha_LUMO,beta_HOMO,beta_LUMO)
   lEI,lCP,lCH,ASD = calc_lEI(gEI,gCP,gCH,input_file)
   ofs_name= input_file[:-4]+'.ENIndex' 
   ofs = open(ofs_name, 'w')
   ofs.write("Global Electrophilicity Index:    %3.2f ev \n" % float(gEI))
   ofs.write("Global Chemical Potential:       %3.2f ev \n" % float(gCP))
   ofs.write("Global Chemical Hardness:         %3.2f ev \n" % float(gCH))
   ofs.write("Local Electrophilicity Index:     %3.2f ev \n" % float(lEI))
   ofs.write("Local Radical Parr function:      %3.2f  \n" % float(ASD))
   ofs.write("Local Chemical Potential:        %3.2f ev \n" % float(lCP))
   ofs.write("Local Chemical Hardness:          %3.2f ev \n" % float(lCH))
   ofs.close()
            
   print ('********************************************')
   print ( ofs_name + ' is finished on there!')
   print ('********************************************')



