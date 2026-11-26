# -*- coding: utf-8 -*-
import os
import sys
import json
import subprocess
import webbrowser

BASE_DIR = r"C:\Users\Admin\Downloads\Pokedaichien"
JSON_PATH = os.path.join(BASE_DIR, "fashion_data.json")
HTML_PATH = os.path.join(BASE_DIR, "view_fashion.html")
UMODEL = r"C:\Tools\umodel\umodel_64.exe"

def main():
    if not os.path.exists(JSON_PATH):
        print("[-] Khong tim thay fashion_data.json! Hay chay process_all_fashion.py truoc.")
        return
        
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 72)
        print("  POKEDAICHIEN 3D FASHION & CHARACTER VIEWER")
        print("  Tong cong 164 Thoi Trang, Huan Luyen Vien va Quan Quan")
        print("=" * 72)
        print()
        print("  [W] Mo Giao Dien Web Trinh Duyet Truc Quan (view_fashion.html)")
        print("  [T] Xem Danh Sach Toan Bo (danh_sach_FASHION.txt)")
        print()
        print("  --- [CAC THOI TRANG SU KIEN & MASTER TIEU BIEU] ---")
        print("  [1] Cynthia / Truc Lan (Quan quan Sinnoh - HT_ZJ_ZhuLanSDZ)")
        print("  [2] Serena (Giang Sinh - HT_ZJ_Serena)")
        print("  [3] Red (Huyen Thoai Trainer Red - HT_ZJ_ChuanQiChiHong)")
        print("  [4] Elaine (Nu chinh Eevee Pallet - HT_ZJ_XiaoQuYiBu)")
        print("  [5] Chase (Nam chinh Pikachu Let's Go - HT_ZJ_XiaoShengFangKeMeng)")
        print("  [6] Steven Stone / Dai Ngo (Quan quan Hoenn - HT_ZJ_DaWu)")
        print("  [7] Lance / Do (Quan quan Long Vuong - HT_ZJ_LongKui)")
        print("  [8] Giovanni / Ban Muc (Trum Doi Hoa Tien - HT_ZJ_BanMuLaoDa)")
        print("  [9] Jessie & James (Musashi & Kojiro Doi Hoa Tien)")
        print("  [10] Lillie (Z-Powered Form - HT_ZJ_LiLiAi)")
        print("  [11] Nessa / Lo Ly Na (Thu linh Dao quan Nuoc - HT_ZJ_LuLiNa)")
        print("  [12] N (Team Plasma - HT_ZJ_N)")
        print("  [13] Cyrus / Xich Nhat (Trum Team Galactic - HT_ZJ_ChiRi)")
        print("  [14] Ghetsis / Khoi Ky Tu (Trum Team Plasma - HT_ZJ_KuiQiSi)")
        print("  [15] Archie / Thuy Ngo Dong (Trum Team Aqua - HT_ZJ_ShuiWuTong)")
        print("  [16] Maxie / Xich Diem Tung (Trum Team Magma - HT_NPC_ChiYanSong)")
        print("  [17] Hatsune Miku & Rem & Ram Crossover (HT_NPC_ChuYin / LeiMu / LaMu)")
        print()
        print("  [0] Thoat")
        print()
        print("  Hoac NHAP TRUC TIEP ID (1-164) hoac Ma file UPK:")
        opt = input("  Nhap lua chon cua ban: ").strip()
        
        if opt == "0":
            break
        elif opt.upper() == "W":
            webbrowser.open("file:///" + HTML_PATH.replace("\\", "/"))
            continue
        elif opt.upper() == "T":
            os.system(f'notepad "{os.path.join(BASE_DIR, "danh_sach_FASHION.txt")}"')
            continue
            
        quick_map = {
            "1": "decrypted_effects/3359567186.upk",
            "2": "decrypted_effects/2775821357.upk",
            "3": "decrypted_effects/1808458874.upk",
            "4": "decrypted_effects/1921945583.upk",
            "5": "decrypted_effects/4106722328.upk",
            "6": "decrypted_effects/3467064008.upk",
            "7": "decrypted_effects/1854680015.upk",
            "8": "decrypted_effects/1240846142.upk",
            "9": "decrypted_effects/4148574356.upk",
            "10": "decrypted_effects/2753063086.upk",
            "11": "decrypted_effects/3467064008.upk",
            "12": "decrypted_effects/677582100.upk",
            "13": "decrypted_effects/1616063893.upk",
            "14": "decrypted_effects/4025031779.upk",
            "15": "decrypted_effects/2460826836.upk",
            "16": "decrypted_effects/931424923.upk",
            "17": "decrypted_effects/533843488.upk",
        }
        
        target_upk = None
        if opt in quick_map:
            target_upk = os.path.join(BASE_DIR, quick_map[opt])
        else:
            # Check ID in data
            if opt.isdigit():
                idx = int(opt)
                if 1 <= idx <= len(data):
                    target_upk = data[idx - 1]['upk_path']
            if not target_upk:
                # Check filename
                cand = opt if opt.endswith(".upk") else opt + ".upk"
                p1 = os.path.join(BASE_DIR, "decrypted_effects", cand)
                p2 = os.path.join(BASE_DIR, "decrypted_models", cand)
                if os.path.exists(p1): target_upk = p1
                elif os.path.exists(p2): target_upk = p2
                
        if target_upk and os.path.exists(target_upk):
            print(f"[+] Dang mo mo hinh 3D trong UModel: {target_upk}")
            subprocess.Popen([UMODEL, "-meshes", target_upk])
            input("\nNhan Enter de tiep tuc...")
        else:
            print(f"[-] Khong tim thay tep phu hop: {opt}")
            input("\nNhan Enter de thu lai...")

if __name__ == "__main__":
    main()
