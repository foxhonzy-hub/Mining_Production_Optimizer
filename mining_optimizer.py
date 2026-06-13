import streamlit as st

# 1. INITIAL PAGE SETTING
st.set_page_config(
    page_title="Mining Production Optimizer v3.1.0",
    page_icon="⛏️",
    layout="wide"
)

# 2. INJEKSI CSS UNTUK TEMA GELAP & KOTAK PRESISI
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
    
    /* Styling Kolom Utama Berwarna Gelap */
    [data-testid="stColumn"] {
        background-color: #161616 !important;
        border: 1px solid #222222 !important;
        border-radius: 10px !important;
        padding: 20px !important;
    }
    
    /* Menghilangkan margin bawaan streamlit agar lebih padat/ringkas */
    .stNumberInput {
        margin-bottom: -10px !important;
    }
    
    /* Memaksa label teks agar rata kiri dan box angka rata kanan secara horizontal */
    .stNumberInput label p {
        color: #aaaaaa !important; 
        font-size: 14px !important;
        font-weight: bold !important;
        margin-top: 8px !important;
    }
    .stNumberInput div div input {
        background-color: #111111 !important;
        color: #ffffff !important;
        border: 1px solid #333333 !important;
        text-align: center !important;
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

# Fungsi Global pembuat baris input berjejer samping (Aman dari NameError)
def make_row(label_text, key_name):
    c_text, c_input = st.columns([2, 1])
    with c_text:
        st.markdown(f"<p style='color:#aaaaaa; font-weight:bold; margin-top:8px;'>{label_text}</p>", unsafe_allow_html=True)
    with c_input:
        return st.number_input(label_text, min_value=0, value=0, step=1, label_visibility="collapsed", key=key_name)


# 3. MEMBUAT 3 KOLOM UTAMA BERJAJAR
col0, col1, col2 = st.columns(3)

# --- KOLOM 1: LEVEL 0 ---
with col0:
    st.markdown("<div style='border-top: 4px solid #f39c12; margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("### Level 0: Raw Materials")
    
    lvl0_copper = make_row("Copper Ore", "l0_cop")
    lvl0_iron = make_row("Iron Ore", "l0_iron")
    lvl0_silver = make_row("Silver Ore", "l0_sil")
    lvl0_gold = make_row("Gold Ore", "l0_gold")
    lvl0_aluminium = make_row("Aluminium Ore", "l0_alum")
    lvl0_coal = make_row("Coal", "l0_coal
