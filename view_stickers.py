# -*- coding: utf-8 -*-
"""
Trình khởi chạy Xem Toàn bộ Sticker & Biểu Tượng Game Pokedaichien
"""
import os
import webbrowser

def main():
    html_path = os.path.abspath("view_stickers.html")
    if os.path.exists(html_path):
        print("=" * 65)
        print("  POKEDAICHIEN - TRÌNH XEM STICKER, AVATAR & TÀI NGUYÊN GAME")
        print("=" * 65)
        print(f"[+] Dang mo bo suu tap Sticker tai: {html_path}")
        webbrowser.open(f"file:///{html_path}")
    else:
        print("[-] Khong tim thay file view_stickers.html!")

if __name__ == "__main__":
    main()
