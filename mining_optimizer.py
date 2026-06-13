import streamlit as st

# 1. SETTING PAGE & LAYOUT WIDE (Agar muat 3 kolom bersanding seperti di gambar)
st.set_page_config(
    page_title="Mining Production Optimizer v3.1.0",
    page_icon="⛏️",
    layout="wide"
)

# 2. INJEKSI CSS CUSTOM (Mengubah tampilan Streamlit menjadi tema gelap & kotak persis di gambar)
st.markdown("""
    <style>
    /* Background Utama */
    .stApp { background-color: #0d0d0d !important; }
    
    /* Judul Aplikasi Atas */
    .main-title {
        color: #f1c40f !important;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        font-size: 32px;
        margin-bottom: 5px;
    }
    .version-text {
        color: #888888 !important;
        text-align: center;
        font-size: 14px;
        margin-bottom: 25px;
    }
    
    /* Style Kotak Level (Card) */
    .level-card {
        background-color: #1a1a1a !important;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        min-height: 750px;
    }
    
    /* Border Atas Berwarna sesuai Gambar */
    .lvl0-box { border-top: 4px solid #f39c12; }
    .lvl1-box { border-top: 4px solid #3498db; }
    .lvl2-box { border-top: 4px solid #e74c3c; }
    
    /* Judul di setiap kolom Level */
    .level-title {
        color: #ffffff !important;
        font-size: 20px !important;
        font-weight: bold !important;
        margin-bottom: 20px !important;
    }
    
    /* Custom Input Box agar Ringkas ke Samping */
    .stNumberInput div div input {
        background-color: #111111 !important;
        color: #ffffff !important;
        border: 1px solid #333333 !important;
        text-align: center;
    }
    label p { color: #aaaaaa !important; font-size: 14px !important; }
    
    /* Kotak Hasil Terminal Hijau di Bagian Bawah */
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

# Headings Utama
st.markdown('<div class="main-title">Mining Production Optimizer</div>', unsafe_allow_html=True)
st.markdown('<div class="version-text">v3.1.0</div>', unsafe_allow_html=True)

# 3. MEMBUAT TIGA KOLOM UTAMA SESUAI GAMBAR
col0, col1, col2 = st.columns(3)

# --- LEVEL 0: RAW MATERIALS ---
with col0:
    st.markdown('<div class="level-card lvl0-box">', unsafe_allow_html=True)
    st.markdown('<p class="level-title">Level 0: Raw Materials</p>', unsafe_allow_html=True)
    
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
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- LEVEL 1: INGOTS & GEMS ---
with col1:
    st.markdown('<div class="level-card lvl1-box">', unsafe_allow_html=True)
    st.markdown('<p class="level-title">Level 1: Ingots & Gems</p>', unsafe_allow_html=True)
    
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
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- LEVEL 2: COMPONENTS ---
with col2:
    st.markdown('<div class="level-card lvl2-box">', unsafe_allow_html=True)
    st.markdown('<p class="level-title">Level 2: Components (Perhiasan Jadi)</p>', unsafe_allow_html=True)
    
    lvl2_gold_ring = st.number_input("Gold Ring", min_value=0, value=0, step=1)
    lvl2_silver_ring = st.number_input("Silver Ring", min_value=0, value=0, step=1)
    lvl2_gold_chain = st.number_input("Gold Chain", min_value=0, value=0, step=1)
    lvl2_silver_chain = st.number_input("Silver Chain", min_value=0, value=0, step=1)
    lvl2_gold_earring = st.number_input("Gold Earring", min_value=0, value=0, step=1)
    lvl2_silver_earring = st.number_input("Silver Earring", min_value=0, value=0, step=1)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# 4. ACTION BUTTON & TERMINAL OUTPUT
if st.button("🚀 HITUNG PRODUKSI OPTIMAL (AI OPTIMIZER)", use_container_width=True):
    
    # --- LOGIKA SIMULASI PELEBURAN (Lvl 0 ke Lvl 1) ---
    # Rumus standard: 5 Ore + Coal -> 1 Ingot Matang
    smelted_gold = min(lvl0_gold // 5, lvl0_coal)
    smelted_silver = min(lvl0_silver // 5, lvl0_coal)
    smelted_diamond = lvl0_diamond // 5  # Permata biasanya tidak butuh coal/tergantung server
    smelted_ruby = lvl0_ruby // 5
    
    # Akumulasi total stok matang di Level 1
    total_gold_ingot = lvl1_gold + smelted_gold
    total_silver_ingot = lvl1_silver + smelted_silver
    total_diamond = lvl1_diamond + smelted_diamond
    total_ruby = lvl1_ruby + smelted_ruby

    # --- LOGIKA CRAFTING OPTIMIZER KEBUTUHAN PERHIASAN ---
    # Rekomendasi pembuatan komponen cincin & kalung berdasarkan stok batu permata yang paling bernilai tinggi
    cincin_emas_diamond = min(total_gold_ingot, total_diamond)
    sisa_gold = total_gold_ingot - cincin_emas_diamond
    sisa_diamond = total_diamond - cincin_emas_diamond
    
    cincin_perak_ruby = min(total_silver_ingot, total_ruby)
    sisa_silver = total_silver_ingot - cincin_perak_ruby
    sisa_ruby = total_ruby - cincin_perak_ruby

    # --- OUTPUT HASIL ALA TERMINAL DI VIDEO ---
    report = "🤖 [AI MINING PRODUCTION OPTIMIZER REPORT]\n"
    report += "======================================================================\n\n"
    
    report += "⚒️  [HASIL PROSES SMELTER (LEVEL 0 -> LEVEL 1)]:\n"
    report += f"   • Berhasil melebur: +{smelted_gold} Gold Ingot & +{smelted_silver} Silver Ingot.\n"
    report += f"   • Berhasil menggosok: +{smelted_diamond} Diamond & +{smelted_ruby} Ruby.\n\n"
    
    report += "💍 [REKOMENDASI CRAFTING TERBAIK (PROFIT MAKSIMAL)]:\n"
    report += "   -------------------------------------------------\n"
    report += f"   • Buat **{cincin_emas_diamond}x Gold Ring (Diamond)** menggunakan Gold Ingot + Diamond.\n"
    report += f"   • Buat **{cincin_perak_ruby}x Silver Ring (Ruby)** menggunakan Silver Ingot + Ruby.\n\n"
    
    report += "📦 [SISA LIMPAHAN BAHAN UNTUK DIJUAL ECERAN]:\n"
    report += "   -------------------------------------------------\n"
    report += f"   • Sisa Bahan: {sisa_gold} Gold Ingot | {sisa_silver} Silver Ingot\n"
    report += f"   • Sisa Permata: {sisa_diamond} Diamond | {sisa_ruby} Ruby\n\n"
    
    report += "💰 [ESTIMASI PROFIT]:\n"
    report += "   Semua bahan sisa disarankan langsung dicairkan ke NPC Balai Kota untuk menghindari penumpukan komponen kosong yang tidak laku dijual!"

    st.markdown(f'<div class="terminal-box">{report}</div>', unsafe_allow_html=True)
