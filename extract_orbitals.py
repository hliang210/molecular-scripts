# -*- coding: utf-8 -*-
# extract_orbitals.py
#
# 这个脚本用于从 Gaussian 输出文件（.log 或 .out）中提取 HOMO 和 LUMO 能级（以 eV 为单位）。
#
# 使用方法（示例）：
#   python extract_orbitals.py my_gaussian_output.log

import sys
import re

def extract_homo_lumo(log_file):
    """
    1. 打开 Gaussian 输出文件
    2. 查找类似于 "Alpha  occ. eigenvalues -- -0.32452 -0.19876 ..." 这一行
    3. 提取最后一个 occ. eigenvalue 作为 HOMO（以 Hartree 为单位）
    4. 查找类似于 "Alpha virt. eigenvalues -- 0.12345 0.34567 ..." 这一行
    5. 提取第一个 virt. eigenvalue 作为 LUMO（以 Hartree 为单位）
    6. 将 Hartree 转换为 eV： 1 Hartree ≈ 27.2114 eV
    7. 输出 HOMO（eV）和 LUMO（eV）
    """
    homo_hartree = None
    lumo_hartree = None

    with open(log_file, 'r') as f:
        for line in f:
            # 匹配占据轨道（occ. eigenvalues）那一行
            if "occ. eigenvalues" in line:
                parts = line.split()
                # 假设最后一个数字是 HOMO
                homo_hartree = float(parts[-1])
            # 匹配虚轨道（virt. eigenvalues）那一行
            if "virt. eigenvalues" in line:
                parts = line.split()
                # 假设第一个数字是 LUMO
                lumo_hartree = float(parts[-1])
    
    if homo_hartree is None or lumo_hartree is None:
        print("Error: Could not find HOMO/LUMO levels in the file.")
        return

    # 转换到 eV
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
