
import pymol 
from pymol import stored
from pymol import cmd, CmdException

def func():
	pep_name=open('peptides_nr.txt',"r")
	peptides=pep_name.readlines()
	i=0

	for x in peptides:
		y=x.rstrip()
		y=y+'_chimera_minimized.pdb'
		y_png=y+'.png'
		peptides[i]=y
		i=i+1
		#print peptides
	peptides.sort()
	for pep_pdb in peptides:
		print pep_pdb
		cmd.load(pep_pdb, 'inputfile')
		modelName='inputfile'
		cmd.show('sticks','%s'%modelName)
		cmd.orient(modelName)
		cmd.bg_color('white')
		cmd.ray( 500 , 340)
		png_name = pep_pdb[:-4] + '_300-100.png'
		cmd.png(("%s")%png_name)
		cmd.delete("all")
	print(str("Done!"))
func()