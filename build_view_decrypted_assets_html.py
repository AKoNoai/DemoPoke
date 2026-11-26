import json
import os
from pathlib import Path

BASE_DIR = Path(r"c:\Users\Admin\Downloads\Pokedaichien")
ASSETS_DIR = BASE_DIR / "decrypted_assets"

CAT_MAP = {
    ("Images", "UI_Icon.bags"): ("bags", "Vật Phẩm & Túi Đồ (Bags)"),
    ("Images", "UI_touxiang.touxiang"): ("touxiang", "Avatar / Ảnh Đại Diện"),
    ("Images", "UI_Icon.skill"): ("skill", "Biểu Tượng Chiêu Thức (Skills)"),
    ("Images", "BG"): ("bg", "Hình Nền & Màn Hình (BG)"),
    ("Images", "misc"): ("misc", "Tài Nguyên Khác (Misc)"),
    ("Images", "Util"): ("misc", "Tài Nguyên Tiện Ích (Util)"),
    ("Music", None): ("music", "Nhạc Nền Game (.MP3)"),
    ("Audio", None): ("audio", "Âm Thanh Hiệu Ứng (.OGG)"),
    ("configs", None): ("configs", "Tệp Cấu Hình (.JSON)"),
}

def main():
    if not ASSETS_DIR.exists():
        print("Error: decrypted_assets not found!")
        return

    items = []
    counts = {"bags": 0, "touxiang": 0, "skill": 0, "bg": 0, "misc": 0, "music": 0, "audio": 0, "configs": 0}
    total_bytes = 0
    config_previews = {}

    for p in sorted(ASSETS_DIR.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(ASSETS_DIR)
        rel_web = "decrypted_assets/" + rel.as_posix()
        parts = rel.parts
        top = parts[0] if len(parts) > 1 else ""
        sub = parts[1] if len(parts) > 2 else None
        sz = p.stat().st_size
        total_bytes += sz
        ext = p.suffix.lower()

        if top == "Images":
            cat, cat_lbl = CAT_MAP.get(("Images", sub), ("misc", f"Ảnh ({sub})"))
            kind = "image"
        elif top == "Music":
            cat, cat_lbl = ("music", "Nhạc Nền Game (.MP3)")
            kind = "audio"
        elif top == "Audio":
            cat, cat_lbl = ("audio", "Âm Thanh Hiệu Ứng (.OGG)")
            kind = "audio"
        elif top == "configs":
            cat, cat_lbl = ("configs", "Tệp Cấu Hình (.JSON)")
            kind = "json"
            try:
                txt = p.read_text(encoding="utf-8", errors="ignore")
                config_previews[rel_web] = txt[:4000] + ("\n... (đã rút gọn hiển thị, nhấn Tải Xuống để xem toàn bộ)" if len(txt) > 4000 else "")
            except Exception:
                config_previews[rel_web] = "(Không đọc được xem trước)"
        else:
            cat, cat_lbl = ("misc", "Khác")
            kind = "other"

        counts[cat] = counts.get(cat, 0) + 1
        # Compact tuple: [rel_web, filename, cat, kind, size_kb]
        items.append([rel_web, p.name, cat, kind, round(sz / 1024.0, 1)])

    total_files = len(items)
    total_mb = round(total_bytes / (1024 * 1024), 2)
    inline_items = json.dumps(items, ensure_ascii=False, separators=(",", ":"))
    inline_cfgs = json.dumps(config_previews, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pokedaichien - Kho Tài Nguyên Giải Mã (decrypted_assets) — Xem & Tải Xuống</title>
    <style>
        :root {{
            --bg-dark: #060a13;
            --bg-card: #111827;
            --accent-blue: #38bdf8;
            --accent-gold: #fbbf24;
            --accent-green: #34d399;
            --accent-purple: #c084fc;
            --accent-pink: #f472b6;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background: radial-gradient(circle at 50% 0%, #172554 0%, var(--bg-dark) 55%);
            color: var(--text-main);
            min-height: 100vh;
            padding-bottom: 80px;
        }}
        header {{
            background: rgba(11, 18, 33, 0.94);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid rgba(56, 189, 248, 0.25);
            padding: 16px 24px;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        }}
        .header-container {{
            max-width: 1650px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .title-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }}
        h1 {{
            font-size: 1.48rem;
            font-weight: 800;
            background: linear-gradient(90deg, #38bdf8, #34d399, #fbbf24);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 0.4px;
        }}
        .subtitle {{
            color: var(--text-muted);
            font-size: 0.87rem;
        }}
        .stats-bar {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}
        .stat-pill {{
            background: rgba(30, 41, 59, 0.88);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 5px 12px;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .stat-pill span.val {{
            color: var(--accent-gold);
            font-weight: 800;
        }}

        /* CONTROLS & TABS */
        .controls-wrapper {{
            max-width: 1650px;
            margin: 18px auto 12px;
            padding: 0 24px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .tabs {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}
        .tab-btn {{
            background: rgba(30, 41, 59, 0.82);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: var(--text-main);
            padding: 8px 14px;
            border-radius: 10px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.83rem;
            transition: all 0.18s;
        }}
        .tab-btn:hover {{
            background: rgba(56, 189, 248, 0.18);
            border-color: var(--accent-blue);
        }}
        .tab-btn.active {{
            background: linear-gradient(135deg, #0284c7, #2563eb);
            border-color: #38bdf8;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.45);
        }}
        .toolbar-row {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.08);
            padding: 10px 14px;
            border-radius: 14px;
        }}
        .search-box {{
            flex: 1;
            min-width: 240px;
            max-width: 420px;
            position: relative;
        }}
        .search-box input {{
            width: 100%;
            background: #0b1120;
            border: 1px solid rgba(56, 189, 248, 0.35);
            color: var(--text-main);
            padding: 8px 14px 8px 36px;
            border-radius: 9px;
            font-size: 0.86rem;
            outline: none;
        }}
        .search-box input:focus {{
            border-color: var(--accent-blue);
            box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
        }}
        .search-icon {{
            position: absolute;
            left: 11px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
        }}
        .tool-actions {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            align-items: center;
        }}
        .sort-select {{
            background: #1e293b;
            color: #f8fafc;
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 8px;
            padding: 7px 10px;
            font-size: 0.81rem;
            font-weight: 600;
            outline: none;
            cursor: pointer;
        }}
        .btn {{
            background: rgba(30, 41, 59, 0.92);
            border: 1px solid rgba(255, 255, 255, 0.16);
            color: #e2e8f0;
            padding: 7px 12px;
            border-radius: 8px;
            font-size: 0.81rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.16s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
        }}
        .btn:hover {{
            background: #334155;
            border-color: var(--accent-blue);
            color: #fff;
        }}
        .btn-primary {{
            background: linear-gradient(135deg, #059669, #10b981);
            border-color: #34d399;
            color: #fff;
        }}
        .btn-primary:hover {{
            background: linear-gradient(135deg, #047857, #059669);
            box-shadow: 0 0 15px rgba(16, 185, 129, 0.45);
        }}
        .btn-primary:disabled {{
            opacity: 0.45;
            cursor: not-allowed;
            box-shadow: none;
        }}

        /* MAIN GRID */
        main {{
            max-width: 1650px;
            margin: 10px auto;
            padding: 0 24px;
        }}
        .status-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 12px;
            font-size: 0.85rem;
            color: var(--text-muted);
        }}
        .asset-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(195px, 1fr));
            gap: 14px;
        }}
        .asset-grid.audio-grid {{
            grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
        }}
        .asset-grid.bg-grid {{
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        }}
        .asset-card {{
            background: rgba(17, 24, 39, 0.92);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 13px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: transform 0.18s, border-color 0.18s, box-shadow 0.18s;
            position: relative;
        }}
        .asset-card:hover {{
            transform: translateY(-3px);
            border-color: rgba(56, 189, 248, 0.55);
            box-shadow: 0 10px 24px rgba(0, 0, 0, 0.55);
        }}
        .asset-card.checked {{
            border: 2px solid var(--accent-green);
            box-shadow: 0 0 18px rgba(52, 211, 153, 0.35);
        }}
        .select-chk {{
            position: absolute;
            top: 8px;
            left: 8px;
            z-index: 5;
            width: 19px;
            height: 19px;
            accent-color: var(--accent-green);
            cursor: pointer;
        }}
        .thumb-box {{
            width: 100%;
            height: 155px;
            background: radial-gradient(circle at 50% 50%, #1e293b, #090d16);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            cursor: pointer;
            position: relative;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        }}
        .bg-grid .thumb-box {{
            height: 185px;
        }}
        .thumb-box img {{
            max-width: 94%;
            max-height: 94%;
            object-fit: contain;
            transition: transform 0.25s;
        }}
        .bg-grid .thumb-box img {{
            width: 100%;
            height: 100%;
            max-width: 100%;
            max-height: 100%;
            object-fit: cover;
        }}
        .asset-card:hover .thumb-box img {{
            transform: scale(1.06);
        }}
        .cat-pill {{
            position: absolute;
            top: 8px;
            right: 8px;
            font-size: 0.66rem;
            font-weight: 700;
            padding: 2px 7px;
            border-radius: 5px;
            background: rgba(15, 23, 42, 0.85);
            color: var(--accent-blue);
            border: 1px solid rgba(56, 189, 248, 0.3);
        }}
        .card-info {{
            padding: 9px 11px 11px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            flex: 1;
        }}
        .file-name {{
            font-family: Consolas, monospace;
            font-size: 0.8rem;
            font-weight: 700;
            color: #f8fafc;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .file-meta {{
            font-size: 0.72rem;
            color: var(--text-muted);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .card-actions {{
            display: flex;
            gap: 6px;
            margin-top: auto;
        }}
        .card-actions .btn {{
            flex: 1;
            justify-content: center;
            padding: 5px 8px;
            font-size: 0.75rem;
        }}
        .audio-box {{
            padding: 16px 14px 10px 34px;
            background: linear-gradient(135deg, #0f172a, #1e293b);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .audio-box audio {{
            width: 100%;
            height: 36px;
        }}
        .json-box {{
            height: 130px;
            padding: 12px 12px 12px 34px;
            background: #0b1120;
            color: #34d399;
            font-family: Consolas, monospace;
            font-size: 0.74rem;
            overflow: hidden;
            cursor: pointer;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }}

        /* PAGINATION */
        .pagination {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 8px;
            margin-top: 24px;
            flex-wrap: wrap;
        }}
        .page-btn {{
            background: #1e293b;
            border: 1px solid rgba(255, 255, 255, 0.14);
            color: #e2e8f0;
            padding: 7px 14px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 700;
            font-size: 0.84rem;
        }}
        .page-btn:hover:not(:disabled) {{
            border-color: var(--accent-blue);
            background: #334155;
        }}
        .page-btn:disabled {{
            opacity: 0.4;
            cursor: not-allowed;
        }}
        .page-info {{
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--accent-gold);
            padding: 0 10px;
        }}

        /* LIGHTBOX MODAL */
        .modal {{
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(4, 7, 15, 0.92);
            backdrop-filter: blur(8px);
            z-index: 1000;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        .modal.open {{
            display: flex;
        }}
        .modal-content {{
            background: #0f172a;
            border: 1px solid rgba(56, 189, 248, 0.45);
            border-radius: 18px;
            max-width: 960px;
            width: 100%;
            max-height: 92vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.85);
        }}
        .modal-header {{
            padding: 14px 20px;
            background: #1e293b;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }}
        .modal-title {{
            font-weight: 800;
            font-size: 1rem;
            color: #fff;
            font-family: Consolas, monospace;
        }}
        .modal-close {{
            background: none;
            border: none;
            color: #94a3b8;
            font-size: 1.6rem;
            cursor: pointer;
            line-height: 1;
        }}
        .modal-close:hover {{ color: #fff; }}
        .modal-body {{
            padding: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: auto;
            min-height: 320px;
            max-height: 68vh;
            background: radial-gradient(circle at 50% 50%, #1e293b, #070b14);
        }}
        .modal-body img {{
            max-width: 100%;
            max-height: 62vh;
            object-fit: contain;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
        }}
        .modal-body pre {{
            width: 100%;
            max-height: 60vh;
            overflow: auto;
            background: #060a13;
            color: #34d399;
            padding: 16px;
            border-radius: 10px;
            font-family: Consolas, monospace;
            font-size: 0.82rem;
            white-space: pre-wrap;
            word-break: break-all;
        }}
        .modal-footer {{
            padding: 12px 20px;
            background: #111827;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
        }}
    </style>
</head>
<body>

<header>
    <div class="header-container">
        <div class="title-row">
            <div>
                <h1>POKEDAICHIEN - KHO TÀI NGUYÊN GIẢI MÃ (DECRYPTED_ASSETS)</h1>
                <div class="subtitle">Xem trực tiếp & tải xuống toàn bộ {total_files:,} tệp hình ảnh UI, Avatar, Icon Chiêu Thức, Hình Nền, Nhạc Nền MP3, Âm Thanh OGG & Cấu Hình JSON</div>
            </div>
            <div class="stats-bar">
                <div class="stat-pill">Tổng Số Tệp: <span class="val">{total_files:,}</span></div>
                <div class="stat-pill">Tổng Dung Lượng: <span class="val">{total_mb} MB</span></div>
                <div class="stat-pill">Hình Ảnh (.JPG): <span class="val">{counts['bags']+counts['touxiang']+counts['skill']+counts['bg']+counts['misc']:,}</span></div>
                <div class="stat-pill">Nhạc & Âm Thanh: <span class="val">{counts['music']+counts['audio']}</span></div>
                <div class="stat-pill">Cấu Hình JSON: <span class="val">{counts['configs']}</span></div>
            </div>
        </div>
    </div>
</header>

<div class="controls-wrapper">
    <div class="tabs">
        <button class="tab-btn active" onclick="setCat('all', this)">🌐 Tất Cả ({total_files:,})</button>
        <button class="tab-btn" onclick="setCat('bags', this)">🎒 Vật Phẩm & Túi Đồ ({counts['bags']:,})</button>
        <button class="tab-btn" onclick="setCat('touxiang', this)">🖼️ Avatar / Ảnh Đại Diện ({counts['touxiang']:,})</button>
        <button class="tab-btn" onclick="setCat('skill', this)">⚡ Icon Chiêu Thức ({counts['skill']:,})</button>
        <button class="tab-btn" onclick="setCat('bg', this)">🏞️ Hình Nền & Màn Hình ({counts['bg']})</button>
        <button class="tab-btn" onclick="setCat('misc', this)">🧩 Tài Nguyên Khác ({counts['misc']})</button>
        <button class="tab-btn" onclick="setCat('music', this)">🎵 Nhạc Nền MP3 ({counts['music']})</button>
        <button class="tab-btn" onclick="setCat('audio', this)">🔊 Âm Thanh OGG ({counts['audio']})</button>
        <button class="tab-btn" onclick="setCat('configs', this)">📄 Cấu Hình JSON ({counts['configs']})</button>
    </div>

    <div class="toolbar-row">
        <div class="search-box">
            <span class="search-icon">🔍</span>
            <input type="text" id="searchInput" placeholder="Tìm tên tệp, mã ID (vd: 1019099744, sp.json, .mp3, .ogg)..." oninput="applyFilters()">
        </div>
        <div class="tool-actions">
            <select id="sortSelect" class="sort-select" onchange="applyFilters()">
                <option value="name_asc">🔤 Tên A ➔ Z</option>
                <option value="size_desc">📦 Dung lượng Lớn ➔ Nhỏ</option>
                <option value="size_asc">🪶 Dung lượng Nhỏ ➔ Lớn</option>
            </select>
            <select id="perPageSelect" class="sort-select" onchange="changePerPage(this.value)">
                <option value="60">60 tệp / trang</option>
                <option value="120" selected>120 tệp / trang</option>
                <option value="240">240 tệp / trang</option>
            </select>
            <button class="btn" onclick="selectPageAll()">☑️ Chọn trang này</button>
            <button class="btn" onclick="clearSelection()">✖️ Bỏ chọn</button>
            <button class="btn btn-primary" id="btnBatchDownload" onclick="downloadSelected()" disabled>⬇️ Tải xuống đã chọn (0)</button>
        </div>
    </div>
</div>

<main>
    <div class="status-bar">
        <span id="statusText">Hiển thị {total_files:,} tệp tài nguyên</span>
        <span>💡 Nhấn vào ảnh để phóng to xem kích thước thật, hoặc tích chọn nhiều tệp để tải xuống hàng loạt</span>
    </div>
    <div class="asset-grid" id="assetGrid"></div>
    <div class="pagination" id="paginationBar"></div>
</main>

<!-- LIGHTBOX / PREVIEW MODAL -->
<div class="modal" id="previewModal" onclick="closeModal()">
    <div class="modal-content" onclick="event.stopPropagation()">
        <div class="modal-header">
            <div class="modal-title" id="modalTitle">Preview</div>
            <button class="modal-close" onclick="closeModal()">&times;</button>
        </div>
        <div class="modal-body" id="modalBody"></div>
        <div class="modal-footer">
            <div style="font-size:0.82rem; color:#94a3b8; font-family:Consolas,monospace;" id="modalMeta"></div>
            <div style="display:flex; gap:8px;">
                <button class="btn" onclick="stepModal(-1)">◀ Tệp Trước</button>
                <button class="btn" onclick="stepModal(1)">Tệp Tiếp ▶</button>
                <a class="btn btn-primary" id="modalDownloadBtn" href="#" download>⬇️ Tải Xuống Tệp Này</a>
            </div>
        </div>
    </div>
</div>

<script>
// [rel_web, filename, cat, kind, size_kb]
const allAssets = {inline_items};
const configPreviews = {inline_cfgs};

const CAT_LABELS = {{
    bags: "Túi Đồ",
    touxiang: "Avatar",
    skill: "Chiêu Thức",
    bg: "Hình Nền",
    misc: "Khác",
    music: "Nhạc MP3",
    audio: "Âm Thanh OGG",
    configs: "JSON"
}};

let currentCat = 'all';
let filteredAssets = [...allAssets];
let currentPage = 1;
let perPage = 120;
let selectedSet = new Set();
let modalIdx = -1;

function setCat(cat, btn) {{
    currentCat = cat;
    currentPage = 1;
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    applyFilters();
}}

function changePerPage(val) {{
    perPage = parseInt(val, 10) || 120;
    currentPage = 1;
    renderPage();
}}

function applyFilters() {{
    const q = document.getElementById('searchInput').value.toLowerCase().trim();
    const sortMode = document.getElementById('sortSelect').value;

    filteredAssets = allAssets.filter(item => {{
        if (currentCat !== 'all' && item[2] !== currentCat) return false;
        if (!q) return true;
        return item[1].toLowerCase().includes(q) || item[0].toLowerCase().includes(q);
    }});

    if (sortMode === 'size_desc') {{
        filteredAssets.sort((a, b) => b[4] - a[4]);
    }} else if (sortMode === 'size_asc') {{
        filteredAssets.sort((a, b) => a[4] - b[4]);
    }} else {{
        filteredAssets.sort((a, b) => a[1].localeCompare(b[1]));
    }}

    currentPage = 1;
    renderPage();
}}

function renderPage() {{
    const total = filteredAssets.length;
    const totalPages = Math.max(1, Math.ceil(total / perPage));
    if (currentPage > totalPages) currentPage = totalPages;

    const start = (currentPage - 1) * perPage;
    const end = Math.min(total, start + perPage);
    const slice = filteredAssets.slice(start, end);

    document.getElementById('statusText').textContent =
        `Đang hiển thị ${{total === 0 ? 0 : start + 1}} – ${{end}} trên tổng số ${{total.toLocaleString()}} tệp (Trang ${{currentPage}}/${{totalPages}})`;

    const grid = document.getElementById('assetGrid');
    grid.className = 'asset-grid' +
        ((currentCat === 'music' || currentCat === 'audio') ? ' audio-grid' : '') +
        (currentCat === 'bg' ? ' bg-grid' : '');

    if (slice.length === 0) {{
        grid.innerHTML = '<div style="grid-column:1/-1; text-align:center; padding:50px; color:#64748b;">Không tìm thấy tệp tài nguyên nào phù hợp.</div>';
        document.getElementById('paginationBar').innerHTML = '';
        return;
    }}

    grid.innerHTML = slice.map((item, localIdx) => {{
        const globalIdx = start + localIdx;
        const [rel, name, cat, kind, szKb] = item;
        const isChecked = selectedSet.has(rel);
        const catLbl = CAT_LABELS[cat] || cat;

        let mediaHtml = '';
        if (kind === 'image') {{
            mediaHtml = `
                <div class="thumb-box" onclick="openModal(${{globalIdx}})">
                    <img src="${{rel}}" alt="${{name}}" loading="lazy">
                    <span class="cat-pill">${{catLbl}}</span>
                </div>`;
        }} else if (kind === 'audio') {{
            mediaHtml = `
                <div class="audio-box">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-size:0.85rem; font-weight:700; color:#38bdf8;">${{cat === 'music' ? '🎵 Nhạc Nền MP3' : '🔊 Hiệu Ứng OGG'}}</span>
                        <span class="cat-pill" style="position:static;">${{szKb}} KB</span>
                    </div>
                    <audio controls preload="none" src="${{rel}}"></audio>
                </div>`;
        }} else {{
            const snippet = (configPreviews[rel] || '').slice(0, 260).replace(/</g, '&lt;');
            mediaHtml = `
                <div class="json-box" onclick="openModal(${{globalIdx}})">
                    <div style="color:#fbbf24; font-weight:700; margin-bottom:6px;">📄 JSON Config (Nhấn để xem)</div>
                    <div>${{snippet}}</div>
                </div>`;
        }}

        return `
        <article class="asset-card ${{isChecked ? 'checked' : ''}}" data-rel="${{rel}}">
            <input type="checkbox" class="select-chk" ${{isChecked ? 'checked' : ''}} onchange="toggleSelect('${{rel}}', this)">
            ${{mediaHtml}}
            <div class="card-info">
                <div class="file-name" title="${{rel}}">${{name}}</div>
                <div class="file-meta">
                    <span>${{catLbl}}</span>
                    <span>💾 ${{szKb}} KB</span>
                </div>
                <div class="card-actions">
                    ${{kind !== 'audio' ? `<button class="btn" onclick="openModal(${{globalIdx}})">🔍 Xem</button>` : ''}}
                    <a class="btn btn-primary" href="${{rel}}" download="${{name}}">⬇️ Tải Xuống</a>
                </div>
            </div>
        </article>`;
    }}).join('');

    renderPagination(totalPages);
}}

function renderPagination(totalPages) {{
    const bar = document.getElementById('paginationBar');
    if (totalPages <= 1) {{
        bar.innerHTML = '';
        return;
    }}
    bar.innerHTML = `
        <button class="page-btn" onclick="goPage(1)" ${{currentPage === 1 ? 'disabled' : ''}}>⏮️ Trang Đầu</button>
        <button class="page-btn" onclick="goPage(${{currentPage - 1}})" ${{currentPage === 1 ? 'disabled' : ''}}>◀ Trang Trước</button>
        <span class="page-info">Trang ${{currentPage}} / ${{totalPages}}</span>
        <button class="page-btn" onclick="goPage(${{currentPage + 1}})" ${{currentPage === totalPages ? 'disabled' : ''}}>Trang Sau ▶</button>
        <button class="page-btn" onclick="goPage(${{totalPages}})" ${{currentPage === totalPages ? 'disabled' : ''}}>Trang Cuối ⏭️</button>
    `;
}}

function goPage(p) {{
    currentPage = p;
    renderPage();
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

// Multi-select & Batch Download
function toggleSelect(rel, chkEl) {{
    if (chkEl.checked) selectedSet.add(rel);
    else selectedSet.delete(rel);
    chkEl.closest('.asset-card').classList.toggle('checked', chkEl.checked);
    updateBatchBtn();
}}

function selectPageAll() {{
    const start = (currentPage - 1) * perPage;
    const end = Math.min(filteredAssets.length, start + perPage);
    for (let i = start; i < end; i++) selectedSet.add(filteredAssets[i][0]);
    updateBatchBtn();
    renderPage();
}}

function clearSelection() {{
    selectedSet.clear();
    updateBatchBtn();
    renderPage();
}}

function updateBatchBtn() {{
    const btn = document.getElementById('btnBatchDownload');
    btn.textContent = `⬇️ Tải xuống đã chọn (${{selectedSet.size}})`;
    btn.disabled = selectedSet.size === 0;
}}

function downloadSelected() {{
    if (selectedSet.size === 0) return;
    const list = Array.from(selectedSet);
    if (list.length > 25 && !confirm(`Bạn đang chọn tải xuống ${{list.length}} tệp cùng lúc. Trình duyệt sẽ yêu cầu cho phép tải nhiều tệp. Bạn có muốn tiếp tục không?`)) {{
        return;
    }}
    list.forEach((rel, idx) => {{
        setTimeout(() => {{
            const a = document.createElement('a');
            a.href = rel;
            a.download = rel.split('/').pop();
            document.body.appendChild(a);
            a.click();
            a.remove();
        }}, idx * 140);
    }});
}}

// Lightbox Modal
function openModal(globalIdx) {{
    if (globalIdx < 0 || globalIdx >= filteredAssets.length) return;
    modalIdx = globalIdx;
    const [rel, name, cat, kind, szKb] = filteredAssets[globalIdx];

    document.getElementById('modalTitle').textContent = `${{name}} — (${{CAT_LABELS[cat] || cat}})`;
    const dlBtn = document.getElementById('modalDownloadBtn');
    dlBtn.href = rel;
    dlBtn.download = name;

    const body = document.getElementById('modalBody');
    const meta = document.getElementById('modalMeta');
    meta.textContent = `Đường dẫn: ${{rel}} | Dung lượng: ${{szKb}} KB`;

    if (kind === 'image') {{
        const img = new Image();
        img.onload = () => {{
            meta.textContent = `Đường dẫn: ${{rel}} | Kích thước: ${{img.naturalWidth}} x ${{img.naturalHeight}} px | Dung lượng: ${{szKb}} KB`;
        }};
        img.src = rel;
        body.innerHTML = '';
        body.appendChild(img);
    }} else if (kind === 'json') {{
        const pre = document.createElement('pre');
        pre.textContent = configPreviews[rel] || '(Tệp JSON)';
        body.innerHTML = '';
        body.appendChild(pre);
    }} else {{
        body.innerHTML = `<audio controls autoplay src="${{rel}}" style="width:100%; max-width:500px;"></audio>`;
    }}

    document.getElementById('previewModal').classList.add('open');
}}

function stepModal(dir) {{
    if (modalIdx === -1 || !filteredAssets.length) return;
    const next = (modalIdx + dir + filteredAssets.length) % filteredAssets.length;
    openModal(next);
}}

function closeModal() {{
    document.getElementById('previewModal').classList.remove('open');
    document.getElementById('modalBody').innerHTML = '';
    modalIdx = -1;
}}

window.addEventListener('keydown', e => {{
    if (!document.getElementById('previewModal').classList.contains('open')) return;
    if (e.key === 'Escape') closeModal();
    else if (e.key === 'ArrowLeft') stepModal(-1);
    else if (e.key === 'ArrowRight') stepModal(1);
}});

// Initial render
applyFilters();
</script>
</body>
</html>
"""
    out_file = BASE_DIR / "view_decrypted_assets.html"
    out_file.write_text(html, encoding="utf-8")
    print(f"Generated {out_file} ({out_file.stat().st_size / 1024:.1f} KB) with {total_files:,} assets ({total_mb} MB)!")

if __name__ == "__main__":
    main()
