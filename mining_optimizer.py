import streamlit as st

# 1. INITIAL PAGE SETTING (WIDE LAYOUT MATCH)
st.set_page_config(
    page_title="Mining Production Optimizer v3.1.0",
    page_icon="⛏️",
    layout="wide"
)

# 2. INJEKSI CSS TOTAL 100% SAMA PERSIS DENGAN UI GAME / GAMBAR
st.markdown("""
    <style>
    /* Background dasar aplikasi */
    .stApp { background-color: #0d0d0d !important; }
    
    /* Judul Utama Atas */
    .main-title {
        color: #f1c40f !important;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        font-size: 28px;
        margin-bottom: 0px;
        letter-spacing: 0.5px;
    }
    .version-text {
        color: #888888 !important;
        text-align: center;
        font-size: 13px;
        margin-bottom: 20px;
    }
    
    /* Box Container Utama untuk Tiap Level (Kotak Abu Gelap Tebal) */
    [data-testid="stColumn"] {
        background-color: #1a1a1a !important;
        border: 1px solid #2d2d2d !important;
        border-radius: 8px !important;
        padding: 15px 15px 25px 15px !important;
    }
    
    /* Header Judul Level */
    .level-title {
        color: #ffffff !important;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        font-size: 20px;
        margin-top: 5px;
        margin-bottom: 20px;
    }
    
    /* KOTAK BARIS ITEM KUSTOM (Sama persis seperti list di gambar) */
    .item-row-container {
        background-color: #242424 !important;
        border-radius: 4px !important;
        padding: 6px 12px !important;
        margin-bottom: 8px !important;
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 40px;
        border: 1px solid #2a2a2a;
    }
    
    /* Label teks item di kiri */
    .item-text-left {
        color: #8a8a8a !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        font-family: 'Arial', sans-serif;
    }
    
    /* MENYEMBUNYIKAN TOMBOL + / - BAWAAN STREAMLIT & MERAPIKAN INPUT BOX */
    .stNumberInput div [data-testid="stNumberInputStepDown"],
    .stNumberInput div [data-testid="stNumberInputStepUp"] {
        display: none !important;
    }
    .stNumberInput div div div input {
        background-color: #0f0f0f !important;
        color: #ffffff !important;
        border: 1px solid #333333 !important;
        border-radius: 4px !important;
        text-align: center !important;
        font-size: 13px !important;
        font-weight: bold !important;
        height: 28px !important;
        width: 65px !important;
        padding: 0px !important;
    }
    .stNumberInput div div {
        border: none !important;
        background-color: transparent !important;
    }
    
    /* Menghapus margin bawaan blok Streamlit agar tidak renggang */
    div[data-testid="stBlock"] {
        margin-bottom: 0px !important;
        padding-bottom: 0px !important;
    }
    
    /* Section Level 3 Grid Lebar */
    .level3-section-title {
        color: #f1c40f !important;
        font-size: 15px !important;
        font-weight: bold !important;
        margin-top: 25px !important;
        margin-bottom: 15px !important;
        border-bottom: 1px solid #2d2d2d;
        padding-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Aplikasi Atas
st.markdown('<div class="main-title">Mining Production Optimizer <span style="font-size:14px; color:#888888; font-weight:normal;">v3.1.0</span></div>', unsafe_allow_html=True)
st.write("")

# 3. CONTEXT REUSABLE COMPONENT (Pembuat baris horizontal presisi)
def render_game_row(label, key_id, default_val=0):
    col_label, col_input = st.columns([4, 1])
    with col_label:
        st.markdown(f'<div style="margin-top: 5px;" class="item-text-left">{label}</div>', unsafe_allow_html=True)
    with col_input:
        val = st.number_input(label, min_value=0, value=default_val, step=1, label_visibility="collapsed", key=key_id)
    return val

# 4. SUSUNAN REKREASI 3 KOLOM UTAMA (IMAGE 1A059D)
c0, c1, c2 = st.columns(3)

# --- KOLOM 1: LEVEL 0 ---
with c0:
    st.markdown("<div style='border-top: 3px solid #f39c12; margin-top:-15px; margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="level-title">Level 0: Raw Materials</div>', unsafe_allow_html=True)
    
    items_l0 = ["Copper Ore", "Iron Ore", "Silver Ore", "Gold Ore", "Aluminium Ore", "Coal", "Empty Bottle", "Uncut Emerald", "Uncut Ruby", "Uncut Sapphire", "Uncut Diamond"]
    stok_l0 = {}
    for i, item in enumerate(items_l0):
        st.markdown('<div class="item-row-container">', unsafe_allow_html=True)
        stok_l0[item] = render_game_row(item, f"l0_in_{i}")
        st.markdown('</div>', unsafe_allow_html=True)

# --- KOLOM 2: LEVEL 1 ---
with c1:
    st.markdown("<div style='border-top: 3px solid #3498db; margin-top:-15px; margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="level-title">Level 1: Ingots & Gems</div>', unsafe_allow_html=True)
    
    items_l1 = ["Gold Ingot", "Silver Ingot", "Iron Ingot", "Copper Ingot", "Aluminium Ingot", "Steel Ingot", "Glass", "Emerald", "Ruby", "Sapphire", "Diamond"]
    stok_l1 = {}
    for i, item in enumerate(items_l1):
        st.markdown('<div class="item-row-container">', unsafe_allow_html=True)
        stok_l1[item] = render_game_row(item, f"l1_in_{i}")
        st.markdown('</div>', unsafe_allow_html=True)

# --- KOLOM 3: LEVEL 2 ---
with c2:
    st.markdown("<div style='border-top: 3px solid #e74c3c; margin-top:-15px; margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="level-title">Level 2: Components</div>', unsafe_allow_html=True)
    
    items_l2 = ["Gold Ring", "Silver Ring", "Gold Chain", "Silver Chain", "Gold Earring", "Silver Earring"]
    stok_l2 = {}
    for i, item in enumerate(items_l2):
        st.markdown('<div class="item-row-container">', unsafe_allow_html=True)
        stok_l2[item] = render_game_row(item, f"l2_in_{i}")
        st.markdown('</div>', unsafe_allow_html=True)


# --- 5. REKREASI GRID LEVEL 3 (BERDASARKAN IMAGE 1933C5) ---
st.markdown('<div class="level3-section-title">LEVEL 3</div>', unsafe_allow_html=True)

# Membuat susunan grid 3 kolom horizontal untuk Level 3
l3_col0, l3_col1, l3_col2 = st.columns(3)

items_l3_c0 = ["Emerald Necklace", "Emerald Ring", "Emerald Earring", "Diamond Earring", "Sapphire Necklace Silver", "Ruby Ring Silver", "Emerald Earring Silver"]
items_l3_c1 = ["Ruby Necklace", "Ruby Ring", "Ruby Earring", "Emerald Necklace Silver", "Diamond Necklace Silver", "Sapphire Ring Silver", "Ruby Earring Silver"]
items_l3_c2 = ["Sapphire Necklace", "Sapphire Ring", "Sapphire Earring", "Ruby Necklace Silver", "Emerald Ring Silver", "Diamond Ring Silver", "Sapphire Earring Silver"]

stok_l3 = {}

with l3_col0:
    for i, item in enumerate(items_l3_c0):
        st.markdown('<div class="item-row-container">', unsafe_allow_html=True)
        stok_l3[item] = render_game_row(item, f"l3_c0_{i}")
        st.markdown('</div>', unsafe_allow_html=True)

with l3_col1:
    for i, item in enumerate(items_l3_c1):
        st.markdown('<div class="item-row-container">', unsafe_allow_html=True)
        stok_l3[item] = render_game_row(item, f"l3_c1_{i}")
        st.markdown('</div>', unsafe_allow_html=True)

with l3_col2:
    for i, item in enumerate(items_l3_c2):
        st.markdown('<div class="item-row-container">', unsafe_allow_html=True)
        stok_l3[item] = render_game_row(item, f"l3_c2_{i}")
        st.markdown('</div>', unsafe_allow_html=True)
