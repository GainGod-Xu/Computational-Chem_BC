#!/data/xuhq/.conda/envs/install/bin/python
import os,math,sys
import openbabel

file1 = sys.argv[1]
file2 = file1[:-4] + ".sdf"

obConversion = openbabel.OBConversion()
obConversion.SetInAndOutFormats("xyz", "sdf")

mol = openbabel.OBMol()
obConversion.ReadFile(mol, file1)   # Open Babel will uncompress automatically
obConversion.WriteFile(mol, file2)

