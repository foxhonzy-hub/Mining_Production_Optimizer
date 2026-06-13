import streamlit as st

# 1. INITIAL PAGE SETTING
st.set_page_config(
    page_title="Mining Production Optimizer v3.1.0",
    page_icon="⛏️",
    layout="wide"
)

# 2. INJEKSI CSS UNTUK MERAPTIKAN DAN MEMPERKECIL UKURAN
st.markdown("""
    <style>
    /* Background Utama Website */
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
    
    /* Styling Kolom Utama Berwarna Gelap & Diperkecil Paddingnya */
    [data-testid="stColumn"] {
        background-color: #161616 !important;
        border: 1px solid #222222 !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }
    
    /* Memaksa jarak vertikal antar input box sekecil mungkin */
    div[data-testid="stBlock"] {
        margin-bottom: -14px !important;
    }
    
    /* Mengatur Gaya Teks Label Kiri */
    .item-label {
        color: #aaaaaa !important;
        font-size: 13px !important;
        font-weight: bold !important;
        margin-top: 5px !important;
        white-space: nowrap;
    }
    
    /* Mengatur Kotak Angka Kanan agar Lebih Pendek dan Ringkas */
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
    
    /* Styling khusus untuk Tabs Streamlit agar senada dengan tema gelap */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #161616 !important;
        border: 1px solid #222222 !important;
        border-radius: 5px 5px 0px 0px !important;
        padding: 8px 20px !important;
        color: #888888 !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #222222 !important;
        color: #f1c40f !important;
        border-bottom: 2px solid #f1c40f !important;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Aplikasi
st.markdown('<div class="main-title">Mining Production Optimizer</div>', unsafe_allow_html=True)
st.markdown('<div class="version-text">v3.1.0</div>', unsafe_allow_html=True)

# 3. MEMBUAT NAVIGASI TAB (INPUT STOK VS EDIT HARGA)
tab_produksi, tab_harga = st.tabs(["⚒️ INPUT STOK PRODUKSI", "💰 EDIT HARGA PASAR"])

# ==========================================
# TAB 1: INPUT STOK PRODUKSI
# ==========================================
with tab_produksi:
    col0, col1, col2 = st.columns(3)

    # --- KOLOM 1: LEVEL 0 ---
    with col0:
        st.markdown("<div style='border-top: 4px solid #f39c12; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
        st.markdown("### Level 0: Raw Materials")
        
        items_l0 = ["Copper Ore", "Iron Ore", "Silver Ore", "Gold Ore", "Aluminium Ore", "Coal", "Empty Bottle", "Uncut Emerald", "Uncut Ruby", "Uncut Sapphire", "Uncut Diamond"]
        stok_l0 = {}
        for i, item in enumerate(items_l0):
            r_text, r_in = st.columns([3, 2])
            r_text.markdown(f'<p class="item-label">{item}</p>', unsafe_allow_html=True)
            stok_l0[item] = r_in.number_input(item, min_value=0, value=0, step=1, label_visibility="collapsed", key=f"stok_l0_{i}")

    # --- KOLOM 2: LEVEL 1 ---
    with col1:
        st.markdown("<div style='border-top: 4px solid #3498db; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
        st.markdown("### Level 1: Ingots & Gems")
        
        items_l1 = ["Gold Ingot", "Silver Ingot", "Iron Ingot", "Copper Ingot", "Aluminium Ingot", "Steel Ingot", "Glass", "Emerald", "Ruby", "Sapphire", "Diamond"]
        stok_l1 = {}
        for i, item in enumerate(items_l1):
            r_text, r_in = st.columns([3, 2])
            r_text.markdown(f'<p class="item-label">{item}</p>', unsafe_allow_html=True)
            stok_l1[item] = r_in.number_input(item, min_value=0, value=0, step=1, label_visibility="collapsed", key=f"stok_l1_{i}")

    # --- KOLOM 3: LEVEL 2 ---
    with col2:
        st.markdown("<div style='border-top: 4px solid #e74c3c; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
        st.markdown("### Level 2: Components")
        
        items_l2 = ["Gold Ring", "Silver Ring", "Gold Chain", "Silver Chain", "Gold Earring", "Silver Earring"]
        stok_l2 = {}
        for i, item in enumerate(items_l2):
            r_text, r_in = st.columns([3, 2])
            r_text.markdown(f'<p class="item-label">{item}</p>', unsafe_allow_html=True)
            stok_l2[item] = r_in.number_input(item, min_value=0, value=0, step=1, label_visibility="collapsed", key=f"stok_l2_{i}")


# ==========================================
# TAB 2: EDIT HARGA PASAR
# ==========================================
with tab_harga:
    hp0, hp1, hp2 = st.columns(3)
    
    with hp0:
        st.markdown("<div style='border-top: 4px solid #f39c12; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
        st.markdown("### Harga Raw Materials")
        harga_l0 = {}
        for i, item in enumerate(items_l0):
            r_text, r_in = st.columns([3, 2])
            r_text.markdown(f'<p class="item-label">{item} ($)</p>', unsafe_allow_html=True)
            harga_l0[item] = r_in.number_input(f"Harga {item}", min_value=0, value=10, step=5, label_visibility="collapsed", key=f"harga_l0_{i}")

    with hp1:
        st.markdown("<div style='border-top: 4px solid #3498db; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
        st.markdown("### Harga Ingots & Gems")
        harga_l1 = {}
        for i, item in enumerate(items_l1):
            r_text, r_in = st.columns([3, 2])
            r_text.markdown(f'<p class="item-label">{item} ($)</p>', unsafe_allow_html=True)
            harga_l1[item] = r_in.number_input(f"Harga {item}", min_value=0, value=50, step=10, label_visibility="collapsed", key=f"harga_l1_{i}")

    with hp2:
        st.markdown("<div style='border-top: 4px solid #e74c3c; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
        st.markdown("### Harga Components")
        harga_l2 = {}
        for i, item in enumerate(items_l2):
            r_text, r_in = st.columns([3, 2])
            r_text.markdown(f'<p class="item-label">{item} ($)</p>', unsafe_allow_html=True)
            harga_l2[item] = r_in.number_input(f"Harga {item}", min_value=0, value=150, step=25, label_visibility="collapsed", key=f"harga_l2_{i}")


st.write("")

# 4. PROSES HITUNG LOGIKA INTEGRASI (MENGGUNAKAN DATA STOK & HARGA)
if st.button("🚀 HITUNG PRODUKSI OPTIMAL (AI OPTIMIZER)", use_container_width=True):
    
    # Ambil nilai stok dari dict untuk kalkulasi ringkas
    gold_ore = stok_l0["Gold Ore"]
    diamond_uncut = stok_l0["Uncut Diamond"]
    gold_ingot_stok = stok_l1["Gold Ingot"]
    
    # Logika Simpel Smelter & Crafting
    smelted_gold = gold_ore // 5
    total_gold_ingot = gold_ingot_stok + smelted_gold
    buat_cincin_emas = min(total_gold_ingot, diamond_uncut // 5)
    
    # Hitung Estimasi Value Berdasarkan Harga Pasar yang Diinput User
    estimasi_cuan = buat_cincin_emas * harga_l2["Gold Ring"]
    
    report = "🤖 [AI MINING PRODUCTION OPTIMIZER REPORT]\n"
    report += "======================================================================\n\n"
    report += "⚒️  [HASIL PROSES PELEBURAN SMELTER]:\n"
    report += f"   • Estimasi peleburan: +{smelted_gold} Gold Ingot & +{stok_l0['Silver Ore'] // 5} Silver Ingot.\n\n"
    report += "💍 [REKOMENDASI CRAFTING BENCH]:\n"
    report += f"   • Buat {buat_cincin_emas}x Gold Ring menggunakan Diamond.\n"
    report += f"   • Potensi Nilai Jual Produk: ${estimasi_cuan:,} (Harga Pasar: ${harga_l2['Gold Ring']}/pcs)\n\n"
    report += "💰 [TIPS PASAR]:\n"
    report += "   Harga komponen stabil. Jual langsung ke NPC atau simpan di Guild Chest jika harga drop!"

    st.markdown(f'<div class="terminal-box">{report}</div>', unsafe_allow_html=True)
