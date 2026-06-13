import streamlit as st

# 1. INITIAL PAGE SETTING
st.set_page_config(
    page_title="Mining Production Optimizer v3.1.0",
    page_icon="⛏️",
    layout="wide"
)

# 2. INJEKSI CSS UNTUK AKURASI VISUAL 100% (DARK AESTHETIC & COMPACT)
st.markdown("""
    <style>
    /* Background Utama */
    .stApp { background-color: #0d0d0d !important; }
    
    /* Judul Utama Atas */
    .main-title {
        color: #f1c40f !important;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        font-size: 26px;
        margin-bottom: 0px;
    }
    .version-text {
        color: #888888 !important;
        text-align: center;
        font-size: 12px;
        margin-bottom: 15px;
    }
    
    /* Box Container Kolom Gelap & Rapat */
    [data-testid="stColumn"] {
        background-color: #161616 !important;
        border: 1px solid #222222 !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }
    
    /* Mengurangi Jarak Spasi Vertikal */
    div[data-testid="stBlock"] {
        margin-bottom: -14px !important;
    }
    
    /* Gaya Teks Label Item Kiri */
    .item-label {
        color: #aaaaaa !important;
        font-size: 13px !important;
        font-weight: bold !important;
        margin-top: 5px !important;
        white-space: nowrap;
    }
    .price-label {
        color: #f1c40f !important;
        font-size: 13px !important;
        font-weight: bold !important;
        margin-top: 5px !important;
        white-space: nowrap;
    }
    
    /* Gaya Input Box Angka Kanan */
    .stNumberInput div div input {
        background-color: #111111 !important;
        color: #ffffff !important;
        border: 1px solid #333333 !important;
        text-align: center !important;
        height: 28px !important;
        font-size: 13px !important;
    }
    
    /* Kotak Hasil Terminal Hijau */
    .terminal-box {
        background-color: #050505 !important;
        color: #2ecc71 !important;
        font-family: 'Courier New', Courier, monospace !important;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #222222;
        white-space: pre-wrap;
        margin-top: 15px;
        font-size: 13px;
    }
    
    /* Tombol Hitung */
    div.stButton > button:first-child {
        background-color: #2ecc71 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: none !important;
        height: 40px;
        font-size: 14px;
    }
    div.stButton > button:first-child:hover { background-color: #27ae60 !important; color: #ffffff !important; }
    
    /* Merapikan posisi Toggle Switcher */
    .stToggle {
        margin-bottom: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Utama
st.markdown('<div class="main-title">Mining Production Optimizer</div>', unsafe_allow_html=True)
st.markdown('<div class="version-text">v3.1.0</div>', unsafe_allow_html=True)

# 3. KUMPULAN DATA ITEM (DATABASE KODE)
items_l0 = ["Copper Ore", "Iron Ore", "Silver Ore", "Gold Ore", "Aluminium Ore", "Coal", "Empty Bottle", "Uncut Emerald", "Uncut Ruby", "Uncut Sapphire", "Uncut Diamond"]
items_l1 = ["Gold Ingot", "Silver Ingot", "Iron Ingot", "Copper Ingot", "Aluminium Ingot", "Steel Ingot", "Glass", "Emerald", "Ruby", "Sapphire", "Diamond"]
items_l2 = ["Gold Ring", "Silver Ring", "Gold Chain", "Silver Chain", "Gold Earring", "Silver Earring"]

# Inisialisasi Storage Data agar bisa dibaca di bagian hitungan
stok_l0, harga_l0 = {}, {}
stok_l1, harga_l1 = {}, {}
stok_l2, harga_l2 = {}, {}

# 4. PEMBUATAN LAYOUT 3 KOLOM UTAMA
col0, col1, col2 = st.columns(3)

# --- KOLOM 1: LEVEL 0 (RAW MATERIALS) ---
with col0:
    st.markdown("<div style='border-top: 4px solid #f39c12; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 0: Raw Materials")
    
    # Tombol Switcher Mode Harga / Mode Stok khusus Kolom 1
    mode_harga_l0 = st.toggle("⚙️ Edit Harga Pasar (Lvl 0)", key="sw_l0")
    st.markdown("---")
    
    for i, item in enumerate(items_l0):
        r_text, r_in = st.columns([3, 2])
        if mode_harga_l0:
            r_text.markdown(f'<p class="price-label">💰 {item} ($)</p>', unsafe_allow_html=True)
            harga_l0[item] = r_in.number_input(f"H_{item}", min_value=0, value=10, step=5, label_visibility="collapsed", key=f"h0_{i}")
            stok_l0[item] = 0 # Default jika sedang tidak diisi
        else:
            r_text.markdown(f'<p class="item-label">{item}</p>', unsafe_allow_html=True)
            stok_l0[item] = r_in.number_input(f"S_{item}", min_value=0, value=0, step=1, label_visibility="collapsed", key=f"s0_{i}")
            harga_l0[item] = 10 # Default fallback harga

# --- KOLOM 2: LEVEL 1 (INGOTS & GEMS) ---
with col1:
    st.markdown("<div style='border-top: 4px solid #3498db; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 1: Ngots & Gems")
    
    # Tombol Switcher Mode Harga / Mode Stok khusus Kolom 2
    mode_harga_l1 = st.toggle("⚙️ Edit Harga Pasar (Lvl 1)", key="sw_l1")
    st.markdown("---")
    
    for i, item in enumerate(items_l1):
        r_text, r_in = st.columns([3, 2])
        if mode_harga_l1:
            r_text.markdown(f'<p class="price-label">💰 {item} ($)</p>', unsafe_allow_html=True)
            harga_l1[item] = r_in.number_input(f"H_{item}", min_value=0, value=50, step=10, label_visibility="collapsed", key=f"h1_{i}")
            stok_l1[item] = 0
        else:
            r_text.markdown(f'<p class="item-label">{item}</p>', unsafe_allow_html=True)
            stok_l1[item] = r_in.number_input(f"S_{item}", min_value=0, value=0, step=1, label_visibility="collapsed", key=f"s1_{i}")
            harga_l1[item] = 50

# --- KOLOM 3: LEVEL 2 (COMPONENTS) ---
with col2:
    st.markdown("<div style='border-top: 4px solid #e74c3c; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 2: Components")
    
    # Tombol Switcher Mode Harga / Mode Stok khusus Kolom 3
    mode_harga_l2 = st.toggle("⚙️ Edit Harga Pasar (Lvl 2)", key="sw_l2")
    st.markdown("---")
    
    for i, item in enumerate(items_l2):
        r_text, r_in = st.columns([3, 2])
        if mode_harga_l2:
            r_text.markdown(f'<p class="price-label">💰 {item} ($)</p>', unsafe_allow_html=True)
            harga_l2[item] = r_in.number_input(f"H_{item}", min_value=0, value=150, step=25, label_visibility="collapsed", key=f"h2_{i}")
            stok_l2[item] = 0
        else:
            r_text.markdown(f'<p class="item-label">{item}</p>', unsafe_allow_html=True)
            stok_l2[item] = r_in.number_input(f"S_{item}", min_value=0, value=0, step=1, label_visibility="collapsed", key=f"s2_{i}")
            harga_l2[item] = 150

st.write("")
st.write("")

# 5. PROSES HITUNG LOGIKA INTEGRASI (MENGGUNAKAN DATA STOK & HARGA AKTIF)
if st.button("🚀 HITUNG PRODUKSI OPTIMAL (AI OPTIMIZER)", use_container_width=True):
    
    # Mengambil nilai aman dari dictionary data aktif
    gold_ore = stok_l0.get("Gold Ore", 0)
    diamond_uncut = stok_l0.get("Uncut Diamond", 0)
    gold_ingot_stok = stok_l1.get("Gold Ingot", 0)
    
    # Perhitungan Smelter & Crafting Bench
    smelted_gold = gold_ore // 5
    total_gold_ingot = gold_ingot_stok + smelted_gold
    buat_cincin_emas = min(total_gold_ingot, diamond_uncut // 5)
    
    # Mengambil variabel harga dinamis yang diinput dari mode sakelar harga pasar
    current_ring_price = harga_l2.get("Gold Ring", 150)
    estimasi_cuan = buat_cincin_emas * current_ring_price
    
    report = "🤖 [AI MINING PRODUCTION OPTIMIZER REPORT]\n"
    report += "======================================================================\n\n"
    report += "⚒️  [HASIL PROSES PELEBURAN SMELTER]:\n"
    report += f"   • Estimasi peleburan: +{smelted_gold} Gold Ingot & +{stok_l0.get('Silver Ore', 0) // 5} Silver Ingot.\n\n"
    report += "💍 [REKOMENDASI CRAFTING BENCH]:\n"
    report += f"   • Buat {buat_cincin_emas}x Gold Ring menggunakan Diamond.\n"
    report += f"   • Potensi Nilai Jual Produk: ${estimasi_cuan:,} (Harga Pasar Aktif: ${current_ring_price}/pcs)\n\n"
    report += "💰 [TIPS PASAR]:\n"
    report += "   Gunakan toggle switch di atas setiap kolom untuk memperbarui harga pasar secara berkala sebelum menekan tombol hitung!"

    st.markdown(f'<div class="terminal-box">{report}</div>', unsafe_allow_html=True)
