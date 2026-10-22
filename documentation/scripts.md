# Script reference

All scripts are Python 2 (PyMOL 1.x and Chimera 1.x) or Bash, and are kept as they were written. File names and paths are set near the top of each script.

## pipeline/

| File | What it does |
|---|---|
| `build_peptide.py` | Reads `peptides.pf` (one sequence per line, one-letter codes). For each sequence it attaches the residues one after another with the backbone angles fixed (extended β conformation by default, phi −139° / psi −135°). It then adds the terminal oxygen (`OXT`), removes hydrogens, and saves `pep_struc/<sequence>.pdb`. |
| `chimera-try1.py` | Runs in Chimera. For each peptide it opens `pep_struc/<sequence>.pdb`, adds hydrogens and charges, runs Chimera's `minimize` command (with its default settings), and writes `pep_struc/<sequence>_minimized.pdb`. |
| `pep_model.py` | Runs both steps in order (`pymol -qc build_peptide.py`, then `chimera --nogui --script chimera-try1.py`) and prints the elapsed time. |
| `peptides.pf` | Example input: 88 peptide sequences. |

**Run:** put the four files in one folder, create an empty `pep_struc/` folder next to them, and run `python pep_model.py`. The Chimera path is hard-coded at the top of `pep_model.py` (`/usr/local/bin/chimera/bin/chimera`), so change it for your install.

`build_peptide.py` can also build other conformations. Its `build_seq(seq, ss=...)` function accepts `helix`, `beta`/`antiparallel`, `parallel`, `3/10` and `polypro`, or explicit `phi=`/`psi=` values. The pipeline calls it with no arguments, so it always builds the extended default.

## capped/

`cap_build.py` is the same builder with an acetyl (**ACE**) group added at the N-terminus and an N-methylamide (**NME**) group at the C-terminus, so the peptide ends are neutral. It adds hydrogens and saves `<sequence>_capped.pdb`. The papers describe free termini (H at the N-terminus, OH at the C-terminus), which is what `pipeline/` produces, so this ACE/NME variant is an alternative for runs where neutral ends are wanted.

The working folder and the peptide list (`file02`) are absolute paths near the top and bottom of the script, so edit them before use.

## fab/

`build_peptide.py` (a different script from the one in `pipeline/`) builds each peptide in `examples/peptides_nr.txt` with PyMOL's `fab` command and saves `<sequence>.pdb` in the current folder. It sets no angles, so it is quicker but gives a less controlled starting structure.

## md/

`gmx_auto.sh` takes every `*.pdb` in its folder and, for each one: builds the topology, boxes and solvates it in TIP3P water, adds ions to 0.15 M, minimises, equilibrates (NVT, then NPT), runs 5 ns of MD, and writes the backbone RMSD (`rmsd_<name>.xvg`).

This is for simulating **peptides on their own** (for example to check how stable a model is). It is not the 20 ns ACE–peptide complex simulation reported in paper 2, and those complex runs are not part of this repository.

The five parameter files it needs are included: `ions.mdp`, `minim.mdp`, `nvt.mdp`, `npt.mdp` and `md_5ns.mdp`.

- Needs GROMACS (`gmx`). The `echo "6"` before `pdb2gmx` picks a force field by its menu number. In the GROMACS 5.x menu, 6 is AMBER99SB-ILDN, but the numbering differs between versions, so check it.
- Each peptide gets a folder named after the **first two characters** of its file name, so two peptides that start with the same two letters would collide. Rename the files first, or change `${i:0:2}`.

## analysis/

| Script | What it does |
|---|---|
| `png_pymol.py` | For every peptide in `peptides_nr.txt`, loads `<sequence>_chimera_minimized.pdb`, shows it as sticks on a white background and saves a ray-traced PNG. The file-name suffix differs from what `chimera-try1.py` writes (`_minimized.pdb`), so rename the files or change the suffix. |

Run it in PyMOL, for example `pymol -qc png_pymol.py`. Figures of docked ACE–peptide complexes are not part of this repository.

## examples/

`peptides_nr.txt` is a list of 255 peptide sequences, used by `fab/build_peptide.py` and `analysis/png_pymol.py`.
