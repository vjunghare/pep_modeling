#!/bin/bash
yourfilenames=`ls *.pdb`
echo $yourfilenames
var1="rmsd_"
var2=".xvg"
slash="/"
for i in ${yourfilenames[@]}
do
    echo "$i"
    mkdir ${i:0:2}
    chmod 777 ${i:0:2}
    dir=$(pwd)
    echo $dir
    #in_dir= $dir$slash$i
    cp *.mdp "$(pwd)"/${i:0:2}/
    cp $i "$(pwd)"/${i:0:2}/
    cd ${i:0:2}
    echo "6"|gmx pdb2gmx -f $i -o fnl_processed.gro -water tip3p
    gmx editconf -f fnl_processed.gro -o fnl_processed.pdb
    gmx editconf -f fnl_processed.gro -o fnl_newbox.pdb -c -d 1.0 -bt cubic
    gmx solvate -cp fnl_newbox.pdb -cs spc216.gro -o fnl_solv.gro -p topol.top
    gmx editconf -f fnl_solv.gro -o fnl_solv.pdb
    gmx grompp -f ions.mdp -c fnl_solv.gro -p topol.top -o ions.tpr
    echo "SOL"|gmx genion -s ions.tpr -o fnl_solv_ions.gro -neutral -conc 0.15 -p topol.top
    gmx grompp -f minim.mdp -c fnl_solv_ions.gro -p topol.top -o em.tpr
    gmx mdrun -v -deffnm em
    gmx editconf -f em.gro -o em.pdb
    gmx grompp -f nvt.mdp -c em.gro -p topol.top -o nvt.tpr
    gmx mdrun -deffnm nvt -v
    gmx grompp -f npt.mdp -c nvt.gro -t nvt.cpt -p topol.top -o npt.tpr -maxwarn 2
    gmx mdrun -deffnm npt -v
    gmx grompp -f md_5ns.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr
    gmx mdrun -deffnm md_0_1 -v
    echo "1", "0"|gmx trjconv -s md_0_1.tpr -f md_0_1.xtc -o traj_final.xtc -pbc mol -ur compact -center
    echo "4", "4"|gmx rms -s md_0_1.tpr -f traj_final.xtc -o $var1${i:0:2}$var2 -tu ns
    cd ..
done
