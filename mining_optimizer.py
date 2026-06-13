import streamlit as st

# 1. INITIAL PAGE SETTING
st.set_page_config(
    page_title="Mining Production Optimizer v3.1.0",
    page_icon="⛏️",
    layout="wide"
)

# 2. INJEKSI CSS PRESISI (DARK MODE & COMPACT SPACING 100% MATCH)
st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d !important; }
    
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
    
    /* Box Container Kolom Gelap Presisi */
    [data-testid="stColumn"] {
        background-color: #161616 !important;
        border: 1px solid #222222 !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }
    
    /* Memangkas Jarak Spasi Vertikal Antar Baris */
    div[data-testid="stBlock"] {
        margin-bottom: -14px !important;
    }
    
    /* Gaya Label Item Akurat */
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
    
    /* Gaya Input Box Angka Pendek Rapi */
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
    </style>
""", unsafe_allow_html=True)

# Judul Utama
st.markdown('<div class="main-title">Mining Production Optimizer</div>', unsafe_allow_html=True)
st.markdown('<div class="version-text">v3.1.0</div>', unsafe_allow_html=True)

# 3. DATABASE ITEM NYATA
items_l0 = ["Copper Ore", "Iron Ore", "Silver Ore", "Gold Ore", "Aluminium Ore", "Coal", "Empty Bottle", "Uncut Emerald", "Uncut Ruby", "Uncut Sapphire", "Uncut Diamond"]
items_l1 = ["Gold Ingot", "Silver Ingot", "Iron Ingot", "Copper Ingot", "Aluminium Ingot", "Steel Ingot", "Glass", "Emerald", "Ruby", "Sapphire", "Diamond"]
items_l2 = ["Gold Ring", "Silver Ring", "Gold Chain", "Silver Chain", "Gold Earring", "Silver Earring"]

# 4. MEMBUAT LAYOUT 3 KOLOM UTAMA BERJAJAR
col0, col1, col2 = st.columns(3)

# --- KOLOM 1: LEVEL 0 (RAW MATERIALS) ---
with col0:
    st.markdown("<div style='border-top: 4px solid #f39c12; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 0: Raw Materials")
    
    # Toggle Switcher 100% Akurat
    mode_harga_l0 = st.toggle("⚙️ Edit Harga Pasar (Lvl 0)", key="tg_l0")
    st.markdown("---")
    
    stok_l0 = {}
    harga_l0 = {}
    
    for i, item in enumerate(items_l0):
        r_text, r_in = st.columns([3, 2])
        if mode_harga_l0:
            r_text.markdown(f'<p class="price-label">💰 {item} ($)</p>', unsafe_allow_html=True)
            harga_l0[item] = r_in.number_input(f"H0_{item}", min_value=0, value=10, step=5, label_visibility="collapsed", key=f"h0_real_{i}")
            # Mengamankan stok_l0 agar tidak hilang/error saat dihitung di background
            stok_l0[item] = st.session_state.get(f"s0_real_{i}", 0)
        else:
            r_text.markdown(f'<p class="item-label">{item}</p>', unsafe_allow_html=True)
            stok_l0[item] = r_in.number_input(f"S0_{item}", min_value=0, value=0, step=1, label_visibility="collapsed", key=f"s0_real_{i}")
            harga_l0[item] = st.session_state.get(f"h0_real_{i}", 10)

# --- KOLOM 2: LEVEL 1 (INGOTS & GEMS) ---
with col1:
    st.markdown("<div style='border-top: 4px solid #3498db; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 1: Ingots & Gems")
    
    mode_harga_l1 = st.toggle("⚙️ Edit Harga Pasar (Lvl 1)", key="tg_l1")
    st.markdown("---")
    
    stok_l1 = {}
    harga_l1 = {}
    
    for i, item in enumerate(items_l1):
        r_text, r_in = st.columns([3, 2])
        if mode_harga_l1:
            r_text.markdown(f'<p class="price-label">💰 {item} ($)</p>', unsafe_allow_html=True)
            harga_l1[item] = r_in.number_input(f"H1_{item}", min_value=0, value=50, step=10, label_visibility="collapsed", key=f"h1_real_{i}")
            stok_l1[item] = st.session_state.get(f"s1_real_{i}", 0)
        else:
            r_text.markdown(f'<p class="item-label">{item}</p>', unsafe_allow_html=True)
            stok_l1[item] = r_in.number_input(f"S1_{item}", min_value=0, value=0, step=1, label_visibility="collapsed", key=f"s1_real_{i}")
            harga_l1[item] = st.session_state.get(f"h1_real_{i}", 50)

# --- KOLOM 3: LEVEL 2 (COMPONENTS) ---
with col2:
    st.markdown("<div style='border-top: 4px solid #e74c3c; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 2: Components")
    
    mode_harga_l2 = st.toggle("⚙️ Edit Harga Pasar (Lvl 2)", key="tg_l2")
    st.markdown("---")
    
    stok_l2 = {}
    harga_l2 = {}
    
    for i, item in enumerate(items_l2):
        r_text, r_in = st.columns([3, 2])
        if mode_harga_l2:
            r_text.markdown(f'<p class="price-label">💰 {item} ($)</p>', unsafe_allow_html=True)
            harga_l2[item] = r_in.number_input(f"H2_{item}", min_value=0, value=150, step=25, label_visibility="collapsed", key=f"h2_real_{i}")
            stok_l2[item] = st.session_state.get(f"s2_real_{i}", 0)
        else:
            r_text.markdown(f'<p class="item-label">{item}</p>', unsafe_allow_html=True)
            stok_l2[item] = r_in.number_input(f"S2_{item}", min_value=0, value=0, step=1, label_visibility="collapsed", key=f"s2_real_{i}")
            harga_l2[item] = st.session_state.get(f"h2_real_{i}", 150)

st.write("")
st.write("")

# 5. PROSES HITUNG LOGIKA INTEGRASI KESELURUHAN (MENGGUNAKAN STATE DATA KEDUA MODE)
if st.button("🚀 HITUNG PRODUKSI OPTIMAL (AI OPTIMIZER)", use_container_width=True):
    
    # Mengambil nilai murni dari state background, dijamin sinkron biarpun sedang di mode harga
    gold_ore = stok_l0.get("Gold Ore", 0)
    silver_ore = stok_l0.get("Silver Ore", 0)
    diamond_uncut = stok_l0.get("Uncut Diamond", 0)
    gold_ingot_stok = stok_l1.get("Gold Ingot", 0)
    silver_ingot_stok = stok_l1.get("Silver Ingot", 0)
    
    # 1. Logika Peleburan Otomatis (Smelter)
    smelted_gold = gold_ore // 5
    smelted_silver = silver_ore // 5
    
    total_gold_ingot = gold_ingot_stok + smelted_gold
    total_silver_ingot = silver_ingot_stok + smelted_silver
    
    # 2. Logika Crafting Bench Terbaik (Gold Ring + Diamond)
    buat_cincin_emas = min(total_gold_ingot, diamond_uncut // 5)
    
    # 3. Ambil Harga Komponen dari State Aktif untuk Hitung Value Keuntungan
    harga_cincin_emas = harga_l2.get("Gold Ring", 150)
    estimasi_cuan = buat_cincin_emas * harga_cincin_emas
    
    # Tampilan Output Laporan Terminal Hijau
    report = "🤖 [AI MINING PRODUCTION OPTIMIZER REPORT]\n"
    report += "======================================================================\n\n"
    report += "⚒️  [HASIL PROSES PELEBURAN SMELTER]:\n"
    report += f"   • Estimasi peleburan: +{smelted_gold} Gold Ingot & +{smelted_silver} Silver Ingot.\n"
    report += f"   • Total Stok Siap Pakai: {total_gold_ingot} Gold Ingot & {total_silver_ingot} Silver Ingot.\n\n"
    report += "💍 [REKOMENDASI CRAFTING BENCH]:\n"
    report += f"   • Buat {buat_cincin_emas}x Gold Ring menggunakan Diamond.\n"
    report += f"   • Potensi Nilai Jual Produk: ${estimasi_cuan:,} (Harga Pasar Aktif: ${harga_cincin_emas}/pcs)\n\n"
    report += "💰 [TIPS PASAR]:\n"
    report += "   Gunakan toggle switch di atas setiap kolom untuk memperbarui harga pasar secara berkala sebelum menekan tombol hitung!"

    st.markdown(f'<div class="terminal-box">{report}</div>', unsafe_allow_html=True)
