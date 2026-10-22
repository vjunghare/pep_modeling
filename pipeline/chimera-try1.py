
from chimera import runCommand as rc # use 'rc' as shorthand for runCommand
from chimera import replyobj # for emitting status messages
import os
wd=os.getcwd()
wd=wd + '/'
#print wd
# change to folder with data files
os.chdir(wd)
pep_name=open(wd+'peptides.pf',"r")
peptides=pep_name.readlines()
pep_name.close()
# gather the names of .pdb files in the folder

#file_names = [fn for fn in peptides]
#file_names.sort()
# loop through the files, opening, processing, and closing each in turn

os.chdir(wd+'pep_struc/')
i =1
print "start"
for fn in peptides:
	fn=fn.rstrip() + '.pdb'
	#print fn
	#print i
	#replyobj.status("Processing " + fn) # show what file we're working on
	rc("open #0 " + fn)
	rc("addh")
	#print "addh done"
	rc("addcharge all")
	#print "addcharge done"
	rc("minimize") # put ligand in front of remainder of molecule
	#print "\nDone\n" # center/zoom ligand # make the surface a little bit see-through
	# save image to a file that ends in .png rather than .pdb
	pdb_name = wd + 'pep_struc/' + fn[:-4] + "_minimized.pdb"
	rc("write format pdb #0 " + pdb_name)
	rc("close session")
	#print "\n\n\n"
	i=i+1
	#if (i<3):
		#break
# uncommenting the line below will cause Chimera to exit when the script is done
#rc("stop now")
