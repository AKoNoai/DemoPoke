"""
Pokedaichien - Menu Chuc Nang & Bieu Tuong Tinh Nang UI Viewer
Chay bang: python view_menu_chuc_nang.py
"""

import os
import sys
import webbrowser

BASE_DIR = r"C:\Users\Admin\Downloads\Pokedaichien"
ICONS_DIR = os.path.join(BASE_DIR, "Xuat_Giao_Dien_UI", "Bieu_Tuong_Tinh_Nang")
HTML_FILE = os.path.join(BASE_DIR, "view_menu_chuc_nang.html")
ROSTER_FILE = os.path.join(BASE_DIR, "danh_sach_BIEU_TUONG_TINH_NANG.txt")

def main():
    while True:
        os.system("cls")
        print("=" * 70)
        print("  POKEDAICHIEN - MENU CHUC NANG & BIEU TUONG TINH NANG (UI ICONS)")
        print(f"  Tong cong: 205 bieu tuong PNG trong suot da giai ma")
        print("=" * 70)
        print()
        print("  [1] Mo Bo Suu Tap Giao Dien Truc Quan (view_menu_chuc_nang.html)")
        print("  [2] Mo thu muc chua 205 anh icon PNG (Bieu_Tuong_Tinh_Nang)")
        print("  [3] Mo danh sach tra cuu chi tiet (danh_sach_BIEU_TUONG_TINH_NANG.txt)")
        print("  [4] Mo Texture Atlas goc (zhujiemian.tga / 2048x2048)")
        print("  [0] Thoat")
        print()
        choice = input("Nhap lua chon cua ban (0-4): ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            if os.path.exists(HTML_FILE):
                print("Dang mo Trinh Duyet Web de xem giao dien...")
                webbrowser.open(HTML_FILE)
            else:
                print("Chua tim thay file HTML.")
            input("\n[Nhan Enter de tiep tuc...]")
        elif choice == "2":
            if os.path.exists(ICONS_DIR):
                os.startfile(ICONS_DIR)
            else:
                print("Chua tim thay thu muc icons.")
            input("\n[Nhan Enter de tiep tuc...]")
        elif choice == "3":
            if os.path.exists(ROSTER_FILE):
                os.startfile(ROSTER_FILE)
            else:
                print("Chua tim thay file roster.")
            input("\n[Nhan Enter de tiep tuc...]")
        elif choice == "4":
            tga_path = os.path.join(BASE_DIR, "Xuat_Giao_Dien_UI", "zhujiemian", "2723450440", "Texture2D", "zhujiemian.tga")
            if os.path.exists(tga_path):
                os.startfile(tga_path)
            else:
                print("Chua tim thay file zhujiemian.tga.")
            input("\n[Nhan Enter de tiep tuc...]")

if __name__ == "__main__":
    main()
