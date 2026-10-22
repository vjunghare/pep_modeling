# pep_modeling

An automated pipeline that builds 3D models of short peptides from their sequences and energy-minimises them, so a whole list of peptides can be modelled in one run. Developed for the peptide work at the **Hazra Lab, IIT Roorkee**.

```
peptide sequences      PyMOL: build each      Chimera: add H,        minimised
(one per line)    →    peptide residue by  →  charges, minimise  →   3D models
                       residue                                       (PDB, one per peptide)
```

1. **Build** each peptide residue by residue with PyMOL's Python API, and add the terminal groups.
2. **Minimise** it in UCSF Chimera (steepest descent, then conjugate gradient). Chimera is used so that people without GROMACS installed can still get minimised models.
3. The minimised peptides are then ready for docking (for example with AutoDock Vina) and for structure-based features.

The method is described in two papers (see "How to cite"). The full methodology, with the papers' details, is in [documentation/methodology.md](documentation/methodology.md).

## Quick start

Put `pipeline/build_peptide.py`, `chimera-try1.py`, `pep_model.py` and a `peptides.pf` file (one sequence per line, one-letter codes) in one folder, create an empty `pep_struc/` folder next to them, and run:

```
python pep_model.py
```

Each peptide gets `pep_struc/<sequence>.pdb` (built) and `pep_struc/<sequence>_minimized.pdb` (minimised). The Chimera path is set at the top of `pep_model.py`.

## Layout

| Folder | Purpose |
|---|---|
| `pipeline/` | The pipeline: build in PyMOL, minimise in Chimera |
| `capped/` | Same build, with ACE and NME caps on the termini |
| `fab/` | The simplest build, using PyMOL's `fab` command |
| `md/` | GROMACS script for 5 ns MD of single peptides, with its `.mdp` files |
| `analysis/` | PyMOL script that renders a PNG of each minimised peptide |
| `examples/` | An example list of 255 peptide sequences |
| `documentation/` | Methodology, script reference, and third-party notes |

What each script does, with inputs and outputs: [documentation/scripts.md](documentation/scripts.md).

## Requirements

- **PyMOL** and **UCSF Chimera** 
- **GROMACS**, only for `md/`


## License

Copyright (C) 2026 Vivek Junghare, Hazra Lab, IIT Roorkee. Released under the **GNU General Public License v3.0** (see [LICENSE](LICENSE)).
