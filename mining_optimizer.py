import streamlit as st

# 1. INITIAL PAGE SETTING
st.set_page_config(
    page_title="Mining Production Optimizer v3.1.0",
    page_icon="⛏️",
    layout="wide"
)

# 2. INJEKSI CSS STRUKTURAL (Aman dari Indentation Error)
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
        font-size: 32px;
        margin-bottom: 0px;
    }
    .version-text {
        color: #888888 !important;
        text-align: center;
        font-size: 14px;
        margin-bottom: 25px;
    }
    
    /* Membikin background kolom menjadi kotak gelap aesthetic sesuai gambar */
    [data-testid="stColumn"] {
        background-color: #161616 !important;
        border: 1px solid #222222 !important;
        border-radius: 10px !important;
        padding: 20px !important;
        margin-right: 10px;
    }
    
    /* Mengatur Gaya Teks Label & Input Box agar Rapi Kedalam */
    .stNumberInput label p {
        color: #aaaaaa !important; 
        font-size: 14px !important;
        font-weight: bold !important;
    }
    .stNumberInput div div input {
        background-color: #111111 !important;
        color: #ffffff !important;
        border: 1px solid #333333 !important;
    }
    
    /* Kotak Hasil Terminal Hijau */
    .terminal-box {
        background-color: #050505 !important;
        color: #2ecc71 !important;
        font-family: 'Courier New', Courier, monospace !important;
        padding: 20px;
        border-radius: 5px;
        border: 1px solid #222222;
        white-space: pre-wrap;
        margin-top: 20px;
    }
    
    /* Tombol Hitung Hijau Neon */
    div.stButton > button:first-child {
        background-color: #2ecc71 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: none !important;
        height: 50px;
        font-size: 16px;
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
    st.markdown("<div style='border-top: 4px solid #f39c12; margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 0: Raw Materials")
    lvl0_copper = st.number_input("Copper Ore", min_value=0, value=0, step=1)
    lvl0_iron = st.number_input("Iron Ore", min_value=0, value=0, step=1)
    lvl0_silver = st.number_input("Silver Ore", min_value=0, value=0, step=1)
    lvl0_gold = st.number_input("Gold Ore", min_value=0, value=0, step=1)
    lvl0_aluminium = st.number_input("Aluminium Ore", min_value=0, value=0, step=1)
    lvl0_coal = st.number_input("Coal", min_value=0, value=0, step=1)
    lvl0_bottle = st.number_input("Empty Bottle", min_value=0, value=0, step=1)
    lvl0_emerald = st.number_input("Uncut Emerald", min_value=0, value=0, step=1)
    lvl0_ruby = st.number_input("Uncut Ruby", min_value=0, value=0, step=1)
    lvl0_sapphire = st.number_input("Uncut Sapphire", min_value=0, value=0, step=1)
    lvl0_diamond = st.number_input("Uncut Diamond", min_value=0, value=0, step=1)

# --- KOLOM 2: LEVEL 1 ---
with col1:
    st.markdown("<div style='border-top: 4px solid #3498db; margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 1: Ingots & Gems")
    lvl1_gold = st.number_input("Gold Ingot", min_value=0, value=0, step=1)
    lvl1_silver = st.number_input("Silver Ingot", min_value=0, value=0, step=1)
    lvl1_iron = st.number_input("Iron Ingot", min_value=0, value=0, step=1)
    lvl1_copper = st.number_input("Copper Ingot", min_value=0, value=0, step=1)
    lvl1_aluminium = st.number_input("Aluminium Ingot", min_value=0, value=0, step=1)
    lvl1_steel = st.number_input("Steel Ingot", min_value=0, value=0, step=1)
    lvl1_glass = st.number_input("Glass", min_value=0, value=0, step=1)
    lvl1_emerald = st.number_input("Emerald", min_value=0, value=0, step=1)
    lvl1_ruby = st.number_input("Ruby", min_value=0, value=0, step=1)
    lvl1_sapphire = st.number_input("Sapphire", min_value=0, value=0, step=1)
    lvl1_diamond = st.number_input("Diamond", min_value=0, value=0, step=1)

# --- KOLOM 3: LEVEL 2 ---
with col2:
    st.markdown("<div style='border-top: 4px solid #e74c3c; margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 2: Components")
    lvl2_gold_ring = st.number_input("Gold Ring", min_value=0, value=0, step=1)
    lvl2_silver_ring = st.number_input("Silver Ring", min_value=0, value=0, step=1)
    lvl2_gold_chain = st.number_input("Gold Chain", min_value=0, value=0, step=1)
    lvl2_silver_chain = st.number_input("Silver Chain", min_value=0, value=0, step=1)
    lvl2_gold_earring = st.number_input("Gold Earring", min_value=0, value=0, step=1)
    lvl2_silver_earring = st.number_input("Silver Earring", min_value=0, value=0, step=1)

st.write("")
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
