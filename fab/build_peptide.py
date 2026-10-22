
from pymol import cmd,stored
import os
wd=os.getcwd()
wd=wd + '/'
print wd

def func():
  pep_name=open(wd+'peptides_nr.txt',"r")
  peptides=pep_name.readlines()
  i=0
  for x in peptides:
    y=x.rstrip()
    peptides[i]=y
    i=i+1
    #print peptides
  for seq in peptides:
    cmd.fab(seq, seq)
    pdb_f=seq + '.pdb'
    cmd.save(wd + pdb_f, seq)
  print "Done!"
func()