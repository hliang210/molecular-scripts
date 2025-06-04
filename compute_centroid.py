# compute_centroid.py

import sys

def compute_centroid(xyz_file):
    """
    1. Open XYZ file, ignore the first two lines (number of atoms and comments)
    2. Read atomic labels and coordinates line by line
    3. Calculate the average of all atomic coordinates
    4. Output geometric center
    """
    total_x = 0.0
    total_y = 0.0
    total_z = 0.0
    count = 0

    with open(xyz_file, 'r') as f:
        lines = f.readlines()[2:]  # Skip the first two lines

    for line in lines:
        parts = line.split()
        if len(parts) < 4:
            continue
        # Some XYZ files may have comments，handle exceptions properly
        try:
            x = float(parts[1])
            y = float(parts[2])
            z = float(parts[3])
        except ValueError:
            continue
        total_x += x
        total_y += y
        total_z += z
        count += 1

    if count == 0:
        print("Error: No valid atoms found.")
        return

    centroid = (total_x/count, total_y/count, total_z/count)
    print(f"Centroid (x, y, z): {centroid[0]:.4f}, {centroid[1]:.4f}, {centroid[2]:.4f}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compute_centroid.py <molecule.xyz>")
        sys.exit(1)

    xyz_file = sys.argv[1]
    compute_centroid(xyz_file)
