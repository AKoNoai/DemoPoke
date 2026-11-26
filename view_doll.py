"""
Pokedaichien - Doll Pokemon 3D Viewer (Bup Be / Follow Dolls / 玩偶)
Chay bang: python view_doll.py
"""

import os
import subprocess
import sys

BASE_DIR = r"C:\Users\Admin\Downloads\Pokedaichien"
UMODEL = r"C:\Tools\umodel\umodel_64.exe"
MODELS = os.path.join(BASE_DIR, "decrypted_models")

DOLLS = [
    ("2429411516.upk", "Lapras Doll (Thua Long Bup Be)", "HT_WO_ChengLong", "HT_WO_ChengLong_AnimSet"),
    ("2429130142.upk", "Diancie Doll (De An Hi Bup Be)", "HT_WO_DiAnXi", "HT_WO_DiAnXi_AnimSet"),
    ("2429130142.upk", "Shiny Diancie Doll (De An Hi Sang Choi)", "HT_WO_DiAnXi_SG", "HT_WO_DiAnXi_AnimSet"),
    ("830659883.upk",  "Ho-Oh Doll (Phuong Hoang Lua Bup Be)", "HT_WO_FengWang", "HT_WO_FengWang_AnimSet"),
    ("830659883.upk",  "Shiny Ho-Oh Doll (Phuong Hoang Sang Choi)", "HT_WO_ShanGuangFengWang", "HT_WO_FengWang_AnimSet"),
    ("3671187281.upk", "Groudon Doll (Co Lap Da Bup Be)", "HT_WO_GuLaDuo", "HT_WO_GuLaDuo_AnimSet"),
    ("3671187281.upk", "Shiny Groudon Doll (Co Lap Da Sang Choi)", "HT_WO_GuLaDuo_SG", "HT_WO_GuLaDuo_AnimSet"),
    ("3142109397.upk", "Golden Magikarp Doll (Ca Chep Vang Bup Be)", "HT_WO_HuangJinLiYuWang", "HT_WO_HuangJinLiYuWang_AnimSet"),
    ("2218207829.upk", "Torchic Doll (Ga Lua Bup Be)", "HT_WO_HuoZhiJi", "HT_WO_HuoZhiJi_AnimSet"),
    ("1576213524.upk", "Meowth Doll (Meo Meowth Bup Be)", "HT_WO_MiaoMiao", "HT_WO_MiaoMiao_AnimSet"),
    ("2745930148.upk", "Palkia Doll (Phach Lo Ky A Bup Be)", "HT_WO_PaLuQiYa", "HT_WO_PaLuQiYa_AnimSet"),
    ("2745930148.upk", "Shiny Palkia Doll (Phach Lo Ky A Sang Choi)", "HT_WO_PaLuQiYa_SG", "HT_WO_PaLuQiYa_AnimSet"),
    ("3912423228.upk", "Mega Charizard X Doll (Rong Lua Den X)", "HT_WO_PenHuoLongX", "HT_WO_PenHuoLongX_AnimSet"),
    ("3912423228.upk", "Shiny Mega Charizard X Doll (Rong Lua X Sang Choi)", "HT_WO_PenHuoLongX_SG", "HT_WO_PenHuoLongX_AnimSet"),
    ("1343354218.upk", "Clefairy Doll (Bi Bi Tinh Bup Be)", "HT_WO_PiPiJing", "HT_WO_PiPiJing_AnimSet"),
]

def open_doll(upk, desc, mesh, animset):
    path = os.path.join(MODELS, upk)
    if not os.path.exists(path):
        print(f"  [!] File khong ton tai: {path}")
        return
        
    cmd = [UMODEL, "-meshes"]
    if animset:
        cmd.append(f"-anim={animset}")
    cmd.append(path)
    if mesh:
        cmd.append(mesh)
        
    print(f"\n  [>] Dang mo Doll: {desc}")
    print(f"      + File   : {upk}")
    print(f"      + Mesh   : {mesh}")
    print(f"      + AnimSet: {animset}")
    print("  ================================================================")
    print("  HUONG DAN XEM ANIMATION BUP BE:")
    print("    - Phim ]     : Chon dang dung yen (Idle) hoac chay (Run)")
    print("    - Phim SPACE : Bat / Tat chuyen dong (Play / Pause)")
    print("    - Phim X     : Chay lap lai lien tuc (Loop)")
    print("  ================================================================")
    subprocess.Popen(cmd)

def main():
    while True:
        os.system("cls")
        print("=" * 70)
        print("  POKEDAICHIEN - HE THONG BUP BE DI THEO (DOLL / FOLLOW DOLLS / 玩偶)")
        print("=" * 70)
        print()
        for i, (upk, desc, mesh, anim) in enumerate(DOLLS, 1):
            print(f"  [{i:02d}] {desc}")
            print(f"       Mesh: {mesh} | UPK: {upk}")
        print()
        print("  [D] Mo danh sach chi tiet (danh_sach_DOLL.txt)")
        print("  [0] Thoat")
        print()
        choice = input(f"Nhap lua chon cua ban (1-{len(DOLLS)}): ").strip()
        
        if choice == "0":
            break
        elif choice.upper() == "D":
            os.startfile(os.path.join(BASE_DIR, "danh_sach_DOLL.txt"))
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(DOLLS):
                item = DOLLS[idx]
                open_doll(item[0], item[1], item[2], item[3])
                input("\n  [Nhan Enter de tiep tuc...]")

if __name__ == "__main__":
    main()
