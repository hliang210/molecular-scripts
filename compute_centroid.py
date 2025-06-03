# compute_centroid.py
#
# 这个脚本用于从一个简单的 XYZ 格式文件中读取原子坐标，并计算分子的几何中心 (centroid)。

import sys

def compute_centroid(xyz_file):
    """
    1. 打开 XYZ 文件，忽略前两行（原子数目和注释）
    2. 逐行读取原子标签和坐标
    3. 计算所有原子坐标的平均值
    4. 输出几何中心
    """
    total_x = 0.0
    total_y = 0.0
    total_z = 0.0
    count = 0

    with open(xyz_file, 'r') as f:
        lines = f.readlines()[2:]  # 跳过前两行

    for line in lines:
        parts = line.split()
        if len(parts) < 4:
            continue
        # 部分 XYZ 文件会有注释等，请做好异常处理
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
