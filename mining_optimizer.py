import streamlit as st

# 1. INITIAL PAGE SETTING
st.set_page_config(
    page_title="Mining Production Optimizer v3.1.0",
    page_icon="⛏️",
    layout="wide"
)

# 2. INJEKSI CSS UNTUK MENYESUAIKAN WARNA KOTAK & BACKGROUND
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
    
    /* Memaksa Kotak Container Streamlit Berwarna Gelap Sesuai Gambar */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #161616 !important;
        border: 1px solid #222222 !important;
        border-radius: 10px !important;
        padding: 15px !important;
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
    # Garis penanda warna Oranye di atas judul kolom
    st.markdown("<div style='border-top: 4px solid #f39c12; margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 0: Raw Materials")
    
    # Menggunakan container agar semua input otomatis dibungkus di dalam kotak hitam
    with st.container():
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
    # Garis penanda warna Biru di atas judul kolom
    st.markdown("<div style='border-top: 4px solid #3498db; margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 1: Ingots & Gems")
    
    with st.container():
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
    # Garis penanda warna Merah di atas judul kolom
    st.markdown("<div style='border-top: 4px solid #e74c3c; margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 2: Components")
    
    with st.container():
        lvl2_gold_ring = st.number_input("Gold Ring", min_value=0, value=0, step
