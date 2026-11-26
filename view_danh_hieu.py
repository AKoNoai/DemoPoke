"""
Pokedaichien - He Thong Danh Hieu (Titles / ChengHao / 称号 Viewer)
Chay bang: python view_danh_hieu.py
"""

import os
import subprocess
import sys

BASE_DIR = r"C:\Users\Admin\Downloads\Pokedaichien"
UMODEL = r"C:\Tools\umodel\umodel_64.exe"
MODELS = os.path.join(BASE_DIR, "decrypted_models")

TITLE_PACKAGES = [
    ("2717020828.upk", "Goi Hieu Ung Danh Hieu 3D & Particle (70+ Danh Hieu Hao Quang)"),
    ("1691049805.upk", "Goi Texture Sprite Danh Hieu Goc (Bieu Tuong & Chu Danh Hieu)"),
    ("399217438.upk",  "Goi Hieu Ung Tong Hop ChenghaoEffect (Particle Xoay Quanh Dau)"),
    ("1739455900.upk", "Goi Danh Hieu Thoi Dai & Tran Doanh (ZhenYing Titles)"),
]

def open_title_package(upk, desc):
    path = os.path.join(MODELS, upk)
    if not os.path.exists(path):
        print(f"  [!] File khong ton tai: {path}")
        return
        
    cmd = [UMODEL, path]
    print(f"\n  [>] Dang mo Goi Danh Hieu: {desc}")
    print(f"      + File: {upk}")
    print("  ================================================================")
    print("  HUONG DAN XEM DANH HIEU TRONG UMODEL:")
    print("    - Phim PageUp / PageDown : Chuyen giua cac danh hieu")
    print("    - Phim O                 : Mo danh sach toan bo tai nguyen")
    print("    - Phim Ctrl+X            : Trich xuat danh hieu sang PNG/3D")
    print("  ================================================================")
    subprocess.Popen(cmd)

def main():
    while True:
        os.system("cls")
        print("=" * 70)
        print("  POKEDAICHIEN - HE THONG DANH HIEU (TITLES / CHENGHAO / 称号)")
        print("=" * 70)
        print()
        for i, (upk, desc) in enumerate(TITLE_PACKAGES, 1):
            print(f"  [{i}] {desc}")
            print(f"      Goi UPK: {upk}")
            print()
        print("  [D] Mo danh sach tra cuu toan bo Danh Hieu (danh_sach_DANH_HIEU.txt)")
        print("  [0] Thoat")
        print()
        choice = input(f"Nhap lua chon cua ban (1-{len(TITLE_PACKAGES)}): ").strip()
        
        if choice == "0":
            break
        elif choice.upper() == "D":
            os.startfile(os.path.join(BASE_DIR, "danh_sach_DANH_HIEU.txt"))
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(TITLE_PACKAGES):
                item = TITLE_PACKAGES[idx]
                open_title_package(item[0], item[1])
                input("\n  [Nhan Enter de tiep tuc...]")

if __name__ == "__main__":
    main()
