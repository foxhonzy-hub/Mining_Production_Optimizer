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
    st.markdown("<div style='border-top: 4px solid #f39c12; margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 0: Raw Materials")
    
    with st.container():
