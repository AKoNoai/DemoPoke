"""
Pokedaichien - Thu Cuoi Pokemon Viewer (Mounts / Rideable / ZuoQi)
=================================================================
File UPK chinh: 1457681642.upk (2.3 MB)
Chua TOAN BO 32 mo hinh 3D thu cuoi (HT_ZQ_*) voi 28 AnimSet rieng.

Chay bang: python view_thu_cuoi.py
"""

import os
import subprocess
import sys

BASE_DIR = r"C:\Users\Admin\Downloads\Pokedaichien"
UMODEL = r"C:\Tools\umodel\umodel_64.exe"
MODELS = os.path.join(BASE_DIR, "decrypted_models")
MOUNT_UPK = "1457681642.upk"

# Danh sach TOAN BO 32 thu cuoi trong game
# (mesh_name, animset_name, ten_viet, loai)
MOUNTS = [
    # === NHOM 1: THU CUOI BO HANH / DAT LIEN ===
    ("HT_ZQ_GaiOuKa",         "HT_ZQ_GaiOuKa_AnimSet",         "Groudon (Cai Ou Ka - Than Dat)",          "DAT"),
    ("HT_ZQ_ShangGuangGaiOuKa","HT_ZQ_GaiOuKa_AnimSet",        "Shiny Groudon (Than Dat Sang Choi)",       "DAT"),
    ("HT_ZQ_BanJiLa",         "HT_ZQ_BanJiLa_AnimSet",         "Tyranitar (Ban Ji La - Khung Long Giap)",  "DAT"),
    ("HT_ZQ_MegaBanJiLa",     "HT_ZQ_MegaBanJiLa_AnimSet",     "Mega Tyranitar (Sieu Tien Hoa)",           "DAT"),
    ("HT_ZQ_GuLeDun",         "HT_ZQ_GuLeDun_AnimSet",         "Koraidon (Co Lac Don - Xe Mo To Gen 9)",   "DAT"),
    ("HT_ZQ_MiLeDun",         "HT_ZQ_MiLeDun_AnimSet",         "Miraidon (Mat Lac Don - Xe Dien Gen 9)",   "DAT"),
    ("HT_ZQ_HouJingWang",     "HT_ZQ_HouJingWang_AnimSet",     "Infernape (Hou Jing Wang - Vua Khi Lua)",  "DAT"),
    ("HT_ZQ_TieJiaXiNiu",     "HT_ZQ_TieJiaXiNiu_AnimSet",     "Rhyperior (Niu Sat Giap Thep)",            "DAT"),
    ("HT_ZQ_ZuoQiShanYang",   "HT_ZQ_ZuoQiShanYang_AnimSet",   "Gogoat (De Nui Cuoi - ShanYang)",          "DAT"),
    ("HT_ZQ_JuQianTangLang",  "HT_ZQ_JuQianTangLang_AnimSet",  "Scizor (Bo Ngua Khong Lo - JuQian)",       "DAT"),
    ("HT_ZQ_GouPaLuWeng",     "HT_ZQ_GouPaLuWeng_AnimSet",     "Drapion (Bich Rua Doc - GouPaLuWeng)",     "DAT"),

    # === NHOM 2: THU CUOI BAY / TREN KHONG ===
    ("HT_ZQ_LaDiYaSi",        "HT_ZQ_LaDiYaSi_AnimSet",        "Latias (Phi Thuyen Do - LaDiYaSi)",        "BAY"),
    ("HT_ZQ_ShanGuangLaDiYaSi","HT_ZQ_LaDiYaSi_AnimSet",       "Shiny Latias (Sang Choi LaDiYaSi)",        "BAY"),
    ("HT_ZQ_KeLeiSeLiYa",     "HT_ZQ_KeLeiSeLiYa_AnimSet",     "Cresselia (Than Trang - KeLeiSeLiYa)",     "BAY"),
    ("HT_ZQ_LuNaiYaLa",       "HT_ZQ_LuNaiYaLa_AnimSet",       "Lunala (Than Mat Trang - LuNaiYaLa)",      "BAY"),
    ("HT_ZQ_SuoErJiaLeiOu",   "HT_ZQ_SuoErJiaLeiOu_AnimSet",   "Solgaleo (Than Mat Troi - SuoErJiaLeiOu)", "BAY"),
    ("HT_ZQ_ZheErNiYaSi",     "HT_ZQ_ZheErNiYaSi_AnimSet",     "Zerneas (Than Su Song - ZheErNiYaSi)",     "BAY"),
    ("HT_ZQ_GuLaDuo",         "HT_ZQ_GuLaDuo_AnimSet",         "Groudon Bay (GuLaDuo Chien - Bay)",        "BAY"),
    ("HT_ZQ_FeiJi_K",         "HT_ZQ_FeiJi_K_AnimSet",         "May Bay / Phi Co (FeiJi_K)",               "BAY"),
    ("HT_ZQ_GuanGuangQiu",    "HT_ZQ_GuanGuangQiu_AnimSet",    "Khinh Khi Cau (GuanGuangQiu)",             "BAY"),
    ("HT_ZQ_Guiwang",         "HT_ZQ_Guiwang_AnimSet",         "Than Ma Quy (Guiwang - Ghost King)",       "BAY"),

    # === NHOM 3: THU CUOI XE MAY / PHUONG TIEN ===
    ("HT_ZQ_MoTuoXi",         "HT_ZQ_MoTuoXi_AnimSet",         "Xe Mo To Xi (Moto Phong Cach)",            "XE"),
    ("HT_ZQ_MoTuoChe02_K",    "HT_ZQ_MoTuoChe02_K_AnimSet",    "Xe Mo To K (MoTuoChe02_K)",                "XE"),
    ("HT_ZQ_Motuohong",       "HT_ZQ_Motuohong_AnimSet",       "Xe Mo To Hong (Motuohong)",                "XE"),

    # === NHOM 4: THU CUOI DAC BIET / HUYEN THOAI ===
    ("HT_ZQ_JDPiKaQiu",       "HT_ZQ_JDPiKaQiu_AnimSet",       "Pikachu Cuoi (JD PiKaQiu - Pikachu)",     "DACBIET"),
    ("HT_ZQ_JiQiRen_K",       "HT_ZQ_JiQiRen_K_AnimSet",       "Robot Chien Dau (JiQiRen_K - Mech)",       "DACBIET"),
    ("HT_ZQ_BiLiJiWen",       "HT_ZQ_BiLiJiWen_AnimSet",       "Buzzwole/Pheromosa (BiLiJiWen)",           "DACBIET"),
    ("HT_ZQ_DaiLaJiWeng",     "HT_ZQ_DaiLaJiWeng_AnimSet",     "Dialga Ride (DaiLaJiWeng - Than Thoi Gian)", "DACBIET"),

    # === NHOM 5: THU CUOI YEN NGUA DAC BIET ===
    ("HT_ZQ_YouWeiXuanYuCi",  "HT_ZQ_YouWeiXuanYuCi_AnimSet",  "Comet Steed Ci (YouWeiXuanYuCi)",          "YENNGUA"),
    ("HT_ZQ_ShanGuangYouWeiXuanYuCi", "HT_ZQ_YouWeiXuanYuCi_AnimSet", "Shiny Comet Ci (Sang Choi)",       "YENNGUA"),
    ("HT_ZQ_YouWeiXuanYuXiong","HT_ZQ_YouWeiXuanYuXiong_AnimSet","Comet Steed Xiong (YouWeiXuanYuXiong)",   "YENNGUA"),
    ("HT_ZQ_ShanGuangYouWeiXuanYuXiong","HT_ZQ_YouWeiXuanYuXiong_AnimSet","Shiny Comet Xiong (Sang Choi)", "YENNGUA"),
]

GROUP_NAMES = {
    "DAT":     "THU CUOI MAT DAT (BO HANH / LAND MOUNTS)",
    "BAY":     "THU CUOI BAY TREN KHONG (FLYING MOUNTS)",
    "XE":      "THU CUOI XE MAY / PHUONG TIEN (VEHICLE MOUNTS)",
    "DACBIET": "THU CUOI DAC BIET / HUYEN THOAI (SPECIAL MOUNTS)",
    "YENNGUA": "THU CUOI YEN NGUA / SAO CHOI (COMET STEEDS)",
}

def launch_mount(mesh, animset, desc):
    upk_path = os.path.join(MODELS, MOUNT_UPK)
    if not os.path.exists(upk_path):
        print(f"  [!] Khong tim thay file: {upk_path}")
        return
    cmd = [UMODEL, "-meshes", f"-anim={animset}", upk_path, mesh]
    print(f"\n  [>] Dang mo Thu Cuoi: {desc}")
    print(f"      + Mesh   : {mesh}")
    print(f"      + AnimSet: {animset}")
    print(f"      + File   : {MOUNT_UPK}")
    print("  " + "=" * 60)
    print("  HUONG DAN XEM ANIMATION THU CUOI:")
    print("    - Phim [ ] ]   : Chuyen dong tac Idle/Walk/Run/Fly")
    print("    - Phim SPACE   : Bat/Tat chuyen dong (Play/Pause)")
    print("    - Phim X       : Chay lap lai lien tuc (Loop)")
    print("    - Phim Ctrl+A  : Chuyen doi bo dong tac")
    print("    - Phim S       : Hien/An bo xuong (Skeleton)")
    print("    - Phim B       : Hien ten cac xuong (Bone Names)")
    print("  " + "=" * 60)
    subprocess.Popen(cmd)

def show_group(group_key):
    items = [(i, m) for i, m in enumerate(MOUNTS) if m[3] == group_key]
    while True:
        os.system("cls")
        print("=" * 70)
        print(f"  {GROUP_NAMES[group_key]}")
        print("=" * 70)
        print()
        for idx, (global_idx, (mesh, anim, desc, _)) in enumerate(items, 1):
            print(f"  [{idx:02d}] {desc}")
            print(f"       Mesh: {mesh}")
            print()
        print("  [0] Quay lai menu chinh")
        print()
        choice = input(f"Chon (1-{len(items)}): ").strip()
        if choice == "0" or choice == "":
            break
        if choice.isdigit():
            ci = int(choice) - 1
            if 0 <= ci < len(items):
                _, (mesh, anim, desc, _) = items[ci]
                launch_mount(mesh, anim, desc)
                input("\n  [Nhan Enter de tiep tuc...]")

def main():
    while True:
        os.system("cls")
        print("=" * 70)
        print("  POKEDAICHIEN - HE THONG THU CUOI POKEMON (MOUNTS / ZUOQI)")
        print(f"  File UPK: {MOUNT_UPK} (2.3 MB - Chua toan bo 32 thu cuoi)")
        print("=" * 70)
        print()
        print(f"  [1] Thu cuoi Mat Dat     ({sum(1 for m in MOUNTS if m[3]=='DAT')} con)")
        print(f"  [2] Thu cuoi Bay         ({sum(1 for m in MOUNTS if m[3]=='BAY')} con)")
        print(f"  [3] Thu cuoi Xe May      ({sum(1 for m in MOUNTS if m[3]=='XE')} con)")
        print(f"  [4] Thu cuoi Dac Biet    ({sum(1 for m in MOUNTS if m[3]=='DACBIET')} con)")
        print(f"  [5] Thu cuoi Yen Ngua    ({sum(1 for m in MOUNTS if m[3]=='YENNGUA')} con)")
        print(f"  [6] Xem TAT CA {len(MOUNTS)} thu cuoi")
        print(f"  [7] Mo danh sach chi tiet (danh_sach_THU_CUOI.txt)")
        print("  [0] Thoat")
        print()
        choice = input("Nhap lua chon cua ban (0-7): ").strip()

        if choice == "0":
            break
        elif choice in ("1","2","3","4","5"):
            keys = ["DAT","BAY","XE","DACBIET","YENNGUA"]
            show_group(keys[int(choice)-1])
        elif choice == "6":
            # Hien thi tat ca
            while True:
                os.system("cls")
                print("=" * 70)
                print(f"  TAT CA {len(MOUNTS)} THU CUOI POKEMON DA GIAI MA")
                print("=" * 70)
                print()
                for i, (mesh, anim, desc, cat) in enumerate(MOUNTS, 1):
                    tag = f"[{cat:7s}]"
                    print(f"  [{i:02d}] {tag} {desc}")
                print()
                print("  [0] Quay lai")
                print()
                ch = input(f"Chon (1-{len(MOUNTS)}): ").strip()
                if ch == "0" or ch == "":
                    break
                if ch.isdigit():
                    ci = int(ch) - 1
                    if 0 <= ci < len(MOUNTS):
                        mesh, anim, desc, _ = MOUNTS[ci]
                        launch_mount(mesh, anim, desc)
                        input("\n  [Nhan Enter de tiep tuc...]")
        elif choice == "7":
            roster_path = os.path.join(BASE_DIR, "danh_sach_THU_CUOI.txt")
            if os.path.exists(roster_path):
                os.startfile(roster_path)
            else:
                print("Chua tim thay file danh sach.")
                input("[Nhan Enter de tiep tuc...]")

if __name__ == "__main__":
    main()
