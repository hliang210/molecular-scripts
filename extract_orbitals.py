# -*- coding: utf-8 -*-
# extract_orbitals.py
#
# This script is used to extract HOMO and LUMO energy levels (in eV) from Gaussian output files (. log or. out).

import sys
import re

def extract_homo_lumo(log_file):
    """
    1. Open Gaussian output file
    2. Search for lines similar to "Alpha occ. Eigenvalues ---0.32452-0.19876..."
    3. Extract the last occ. eigenvalue as HOMO (in Hartree units)
    4. Search for lines similar to 'Alpha virt. eigenvalues --0.12345 0.34567...'
    5. Extract the first virt. eigenvalue as LUMO (in Hartree units)
    6. Convert Hartree to eV: 1 Hartree ≈ 27.2114 eV
    7. Output HOMO (eV) and LUMO (eV)
    """
    homo_hartree = None
    lumo_hartree = None

    with open(log_file, 'r') as f:
        for line in f:
            # Match the occupied orbit (occ. eigenvalues) row
            if "occ. eigenvalues" in line:
                parts = line.split()
                # Assuming the last digit is HOMO
                homo_hartree = float(parts[-1])
            # Match the Virt. Eigenvalues line
            if "virt. eigenvalues" in line:
                parts = line.split()
                # Assuming the first number is LUMO
                lumo_hartree = float(parts[-1])
    
    if homo_hartree is None or lumo_hartree is None:
        print("Error: Could not find HOMO/LUMO levels in the file.")
        return

    # Convert to eV
    hartree_to_ev = 27.2114
    homo_ev = homo_hartree * hartree_to_ev
    lumo_ev = lumo_hartree * hartree_to_ev

    print(f"HOMO: {homo_ev:.4f} eV")
    print(f"LUMO: {lumo_ev:.4f} eV")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_orbitals.py <gaussian_output.log>")
        sys.exit(1)

    log_file = sys.argv[1]
    extract_homo_lumo(log_file)
