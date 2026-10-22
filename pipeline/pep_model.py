import os
import time
chimera_path='/usr/local/bin/chimera/bin/chimera'
start = time.time()
os.system('pymol -qc build_peptide.py')
os.system(chimera_path+' --nogui --script chimera-try1.py')
elapsed = time.time() - start
print elapsed
