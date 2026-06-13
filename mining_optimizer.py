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
    </style>
""", unsafe_allow_html=True)

# Judul Aplikasi
st.markdown('<div class="main-title">Mining Production Optimizer</div>', unsafe_allow_html=True)
st.markdown('<div class="version-text">v3.1.0</div>', unsafe_allow_html=True)

# 3. MEMBUAT 3 KOLOM UTAMA BERJAJAR
col0, col1, col2 = st.columns(3)

# --- KOLOM 1: LEVEL 0 ---
with col0:
    st.markdown("<div style='border-top: 4px solid #f39c12; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 0: Raw Materials")
    
    # Baris 1
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Copper Ore</p>', unsafe_allow_html=True)
    lvl0_copper = r_in.number_input("Copper Ore", min_value=0, value=0, step=1, label_visibility="collapsed", key="l0_1")
    
    # Baris 2
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Iron Ore</p>', unsafe_allow_html=True)
    lvl0_iron = r_in.number_input("Iron Ore", min_value=0, value=0, step=1, label_visibility="collapsed", key="l0_2")
    
    # Baris 3
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Silver Ore</p>', unsafe_allow_html=True)
    lvl0_silver = r_in.number_input("Silver Ore", min_value=0, value=0, step=1, label_visibility="collapsed", key="l0_3")
    
    # Baris 4
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Gold Ore</p>', unsafe_allow_html=True)
    lvl0_gold = r_in.number_input("Gold Ore", min_value=0, value=0, step=1, label_visibility="collapsed", key="l0_4")
    
    # Baris 5
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Aluminium Ore</p>', unsafe_allow_html=True)
    lvl0_aluminium = r_in.number_input("Aluminium Ore", min_value=0, value=0, step=1, label_visibility="collapsed", key="l0_5")
    
    # Baris 6
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Coal</p>', unsafe_allow_html=True)
    lvl0_coal = r_in.number_input("Coal", min_value=0, value=0, step=1, label_visibility="collapsed", key="l0_6")
    
    # Baris 7
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Empty Bottle</p>', unsafe_allow_html=True)
    lvl0_bottle = r_in.number_input("Empty Bottle", min_value=0, value=0, step=1, label_visibility="collapsed", key="l0_7")
    
    # Baris 8
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Uncut Emerald</p>', unsafe_allow_html=True)
    lvl0_emerald = r_in.number_input("Uncut Emerald", min_value=0, value=0, step=1, label_visibility="collapsed", key="l0_8")
    
    # Baris 9
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Uncut Ruby</p>', unsafe_allow_html=True)
    lvl0_ruby = r_in.number_input("Uncut Ruby", min_value=0, value=0, step=1, label_visibility="collapsed", key="l0_9")
    
    # Baris 10
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Uncut Sapphire</p>', unsafe_allow_html=True)
    lvl0_sapphire = r_in.number_input("Uncut Sapphire", min_value=0, value=0, step=1, label_visibility="collapsed", key="l0_10")
    
    # Baris 11
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Uncut Diamond</p>', unsafe_allow_html=True)
    lvl0_diamond = r_in.number_input("Uncut Diamond", min_value=0, value=0, step=1, label_visibility="collapsed", key="l0_11")

# --- KOLOM 2: LEVEL 1 ---
with col1:
    st.markdown("<div style='border-top: 4px solid #3498db; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 1: Ingots & Gems")
    
    # Baris 1
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Gold Ingot</p>', unsafe_allow_html=True)
    lvl1_gold = r_in.number_input("Gold Ingot", min_value=0, value=0, step=1, label_visibility="collapsed", key="l1_1")
    
    # Baris 2
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Silver Ingot</p>', unsafe_allow_html=True)
    lvl1_silver = r_in.number_input("Silver Ingot", min_value=0, value=0, step=1, label_visibility="collapsed", key="l1_2")
    
    # Baris 3
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Iron Ingot</p>', unsafe_allow_html=True)
    lvl1_iron = r_in.number_input("Iron Ingot", min_value=0, value=0, step=1, label_visibility="collapsed", key="l1_3")
    
    # Baris 4
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Copper Ingot</p>', unsafe_allow_html=True)
    lvl1_copper = r_in.number_input("Copper Ingot", min_value=0, value=0, step=1, label_visibility="collapsed", key="l1_4")
    
    # Baris 5
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Aluminium Ingot</p>', unsafe_allow_html=True)
    lvl1_aluminium = r_in.number_input("Aluminium Ingot", min_value=0, value=0, step=1, label_visibility="collapsed", key="l1_5")
    
    # Baris 6
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Steel Ingot</p>', unsafe_allow_html=True)
    lvl1_steel = r_in.number_input("Steel Ingot", min_value=0, value=0, step=1, label_visibility="collapsed", key="l1_6")
    
    # Baris 7
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Glass</p>', unsafe_allow_html=True)
    lvl1_glass = r_in.number_input("Glass", min_value=0, value=0, step=1, label_visibility="collapsed", key="l1_7")
    
    # Baris 8
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Emerald</p>', unsafe_allow_html=True)
    lvl1_emerald = r_in.number_input("Emerald", min_value=0, value=0, step=1, label_visibility="collapsed", key="l1_8")
    
    # Baris 9
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Ruby</p>', unsafe_allow_html=True)
    lvl1_ruby = r_in.number_input("Ruby", min_value=0, value=0, step=1, label_visibility="collapsed", key="l1_9")
    
    # Baris 10
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Sapphire</p>', unsafe_allow_html=True)
    lvl1_sapphire = r_in.number_input("Sapphire", min_value=0, value=0, step=1, label_visibility="collapsed", key="l1_10")
    
    # Baris 11
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Diamond</p>', unsafe_allow_html=True)
    lvl1_diamond = r_in.number_input("Diamond", min_value=0, value=0, step=1, label_visibility="collapsed", key="l1_11")

# --- KOLOM 3: LEVEL 2 ---
with col2:
    st.markdown("<div style='border-top: 4px solid #e74c3c; margin-bottom: 5px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 2: Components")
    
    # Baris 1
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Gold Ring</p>', unsafe_allow_html=True)
    lvl2_gold_ring = r_in.number_input("Gold Ring", min_value=0, value=0, step=1, label_visibility="collapsed", key="l2_1")
    
    # Baris 2
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Silver Ring</p>', unsafe_allow_html=True)
    lvl2_silver_ring = r_in.number_input("Silver Ring", min_value=0, value=0, step=1, label_visibility="collapsed", key="l2_2")
    
    # Baris 3
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Gold Chain</p>', unsafe_allow_html=True)
    lvl2_gold_chain = r_in.number_input("Gold Chain", min_value=0, value=0, step=1, label_visibility="collapsed", key="l2_3")
    
    # Baris 4
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Silver Chain</p>', unsafe_allow_html=True)
    lvl2_silver_chain = r_in.number_input("Silver Chain", min_value=0, value=0, step=1, label_visibility="collapsed", key="l2_4")
    
    # Baris 5
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Gold Earring</p>', unsafe_allow_html=True)
    lvl2_gold_earring = r_in.number_input("Gold Earring", min_value=0, value=0, step=1, label_visibility="collapsed", key="l2_5")
    
    # Baris 6
    r_text, r_in = st.columns([3, 2])
    r_text.markdown('<p class="item-label">Silver Earring</p>', unsafe_allow_html=True)
    lvl2_silver_earring = r_in.number_input("Silver Earring", min_value=0, value=0, step=1, label_visibility="collapsed", key="l2_6")

st.write("")

# 4. PROSES HITUNG (LOGIKA INTEGRASI)
if st.button("🚀 HITUNG PRODUKSI OPTIMAL (AI OPTIMIZER)", use_container_width=True):
    
    smelted_gold = lvl0_gold // 5
    smelted_silver = lvl0_silver // 5
    
    total_gold = lvl1_gold + smelted_gold
    total_silver = lvl1_silver + smelted_silver
    
    buat_cincin_emas = min(total_gold, lvl0_diamond // 5)
    
    report = "🤖 [AI MINING PRODUCTION OPTIMIZER REPORT]\n"
    report += "======================================================================\n\n"
    report += "⚒️  [HASIL PROSES PELEBURAN SMELTER]:\n"
    report += f"   • Estimasi peleburan: +{smelted_gold} Gold Ingot & +{smelted_silver} Silver Ingot.\n\n"
    report += "💍 [REKOMENDASI CRAFTING BENCH]:\n"
    report += f"   • Buat {buat_cincin_emas}x Gold Ring menggunakan Diamond.\n\n"
    report += "💰 [TIPS PASAR]:\n"
    report += "   Pastikan untuk selalu memperbarui harga pasar berkala via balai kota NPC!"

    st.markdown(f'<div class="terminal-box">{report}</div>', unsafe_allow_html=True)
