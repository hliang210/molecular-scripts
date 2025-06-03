# Molecular Scripts

This repository contains simple Python scripts for basic computational chemistry tasks:

1. **extract_orbitals.py**  
   - Description: Parses a Gaussian output file and extracts the HOMO and LUMO energy levels (in eV).  
   - Usage: `python extract_orbitals.py <gaussian_output.log>`  
   - Status: Logic implemented, testing and debugging in progress.

2. **compute_centroid.py**  
   - Description: Reads an XYZ-format file and computes the molecular centroid (geometric center).  
   - Usage: `python compute_centroid.py <molecule.xyz>`  
   - Status: Fully functional.

## Future Plans
- Add error handling for different Gaussian output formats.  
- Implement batch processing of multiple output files.  
- Extend to extract excitation energies from TDDFT runs.

