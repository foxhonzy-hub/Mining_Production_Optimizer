import streamlit as st

# 1. SETTING PAGE & TEMA GELAP
st.set_page_config(
    page_title="Mining Production Optimizer - IME Roleplay",
    page_icon="⛏️",
    layout="wide"
)

# 2. INJEKSI CSS CUSTOM (Warna gelap pekat, tombol hijau neon & merah, teks terminal)
st.markdown("""
    <style>
    .stApp { background-color: #1e1e24 !important; }
    h1, h2, h3 { color: #ffffff !important; font-family: 'Arial', sans-serif; font-weight: bold; }
    h1 { text-align: center; margin-bottom: 20px; }
    .stNumberInput div div input { background-color: #2d2d34 !important; color: #ffffff !important; border: 1px solid #555555 !important; }
    label p { color: #e0e0e0 !important; font-weight: 500 !important; }
    
    /* KOTAK HASIL KALKULASI (Terminal Hitam) */
    .terminal-box {
        background-color: #0c0c0d !important;
        color: #33ff33 !important;
        font-family: 'Courier New', Courier, monospace !important;
        padding: 20px;
        border-radius: 5px;
        border: 1px solid #333333;
        white-space: pre-wrap;
        height: 580px;
        overflow-y: auto;
        box-shadow: inset 0 0 10px #000000;
    }
    
    /* TOMBOL HITUNG (Hijau Neon) */
    div.stButton > button:first-child {
        background-color: #2ecc71 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: none !important;
        width: 100%;
        height: 45px;
    }
    div.stButton > button:first-child:hover { background-color: #27ae60 !important; color: #ffffff !important; }
    
    /* TOMBOL RESET (Merah) */
    div.stButton > button.reset-btn {
        background-color: #e74c3c !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border: none !important;
        width: 100%;
        height: 45px;
    }
    div.stButton > button.reset-btn:hover { background-color: #c0392b !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>MINING PRODUCTION OPTIMIZER (FULL LEVEL)</h1>", unsafe_allow_html=True)

# 3. INITIAL DATABASE HARGA PASAR (NPC)
if "prices" not in st.session_state:
    st.session_state.prices = {
        "silver_ore": 30, "gold_ore": 50, "diamond_ore": 80, "ruby_ore": 70, # Lvl 0
        "silver_ingot": 150, "gold_ingot": 300, "diamond": 500, "ruby": 400, # Lvl 1
        "silver_wire": 0, "gold_chain": 0, # Lvl 2 (Tidak laku dijual)
        "silver_diamond_ring": 1200, "gold_ruby_necklace": 1500 # Lvl 3
    }

if "terminal_output" not in st.session_state:
    st.session_state.terminal_output = "Masukkan data inventory Anda, lalu klik 'Hitung Produksi (AI Optimizer)'..."

# 4. TATA LETAK UTAMA (KIRI: INPUT & EDITOR, KANAN: TERMINAL HASIL)
col_left, col_right = st.columns([1.1, 0.9])

with col_left:
    tab1, tab2 = st.tabs(["🎒 INPUT INVENTORY", "⚙️ EDITOR HARGA NPC"])
    
    with tab1:
        st.markdown("### 🪨 Level 0 - Bahan Mentah (Ore / Kasar)")
        c0_1, c0_2 = st.columns(2)
        with c0_1:
            ore_silver = st.number_input("Silver Ore", min_value=0, value=0, step=1)
            ore_gold = st.number_input("Gold Ore", min_value=0, value=0, step=1)
        with c0_2:
            ore_diamond = st.number_input("Uncut Diamond", min_value=0, value=0, step=1)
            ore_ruby = st.number_input("Uncut Ruby", min_value=0, value=0, step=1)
            
        st.markdown("### 🪙 Level 1 - Bahan Matang (Smelted)")
        c1_1, c1_2 = st.columns(2)
        with c1_1:
            ing_silver = st.number_input("Silver Ingot", min_value=0, value=0, step=1)
            ing_gold = st.number_input("Gold Ingot", min_value=0, value=0, step=1)
        with c1_2:
            gem_diamond = st.number_input("Diamond (Clean)", min_value=0, value=0, step=1)
            gem_ruby = st.number_input("Ruby (Clean)", min_value=0, value=0, step=1)

        st.markdown("### 🛠️ Level 2 - Sisa Setengah Jadi (Crafted Component)")
        c2_1, c2_2 = st.columns(2)
        with c2_1:
            comp_wire = st.number_input("Silver Wire / Ring Band", min_value=0, value=0, step=1)
        with c2_2:
            comp_chain = st.number_input("Gold Chain / Frame", min_value=0, value=0, step=1)

    with tab2:
        st.markdown("### 💲 Atur Harga Jual ke Pemerintahan/NPC")
        p = st.session_state.prices
        ce1, ce2 = st.columns(2)
        with ce1:
            p["silver_ore"] = st.number_input("Harga Silver Ore", min_value=0, value=p["silver_ore"])
            p["gold_ore"] = st.number_input("Harga Gold Ore", min_value=0, value=p["gold_ore"])
            p["silver_ingot"] = st.number_input("Harga Silver Ingot", min_value=0, value=p["silver_ingot"])
            p["gold_ingot"] = st.number_input("Harga Gold Ingot", min_value=0, value=p["gold_ingot"])
            p["silver_diamond_ring"] = st.number_input("Harga Silver Diamond Ring (Lvl 3)", min_value=0, value=p["silver_diamond_ring"])
        with ce2:
            p["diamond_ore"] = st.number_input("Harga Uncut Diamond", min_value=0, value=p["diamond_ore"])
            p["ruby_ore"] = st.number_input("Harga Uncut Ruby", min_value=0, value=p["ruby_ore"])
            p["diamond"] = st.number_input("Harga Diamond", min_value=0, value=p["diamond"])
            p["ruby"] = st.number_input("Harga Ruby", min_value=0, value=p["ruby"])
            p["gold_ruby_necklace"] = st.number_input("Harga Gold Ruby Necklace (Lvl 3)", min_value=0, value=p["gold_ruby_necklace"])

with col_right:
    st.markdown("### 📊 HASIL ANALISIS OPTIMAL")
    st.markdown(f'<div class="terminal-box">{st.session_state.terminal_output}</div>', unsafe_allow_html=True)
    st.write("")
    
    # Tombol Kontrol
    btn_c1, btn_c2 = st.columns(2)
    with btn_c1:
        hitung = st.button("Hitung Produksi (AI Optimizer)")
    with btn_c2:
        reset = st.button("Reset Input", key="btn_reset")
        st.markdown("<script>document.querySelectorAll('button')[1].classList.add('reset-btn');</script>", unsafe_allow_html=True)

# 5. LOGIKA PERHITUNGAN AI OPTIMIZER BERTINGKAT
if hitung:
    p = st.session_state.prices
    
    # --- PROSES SIMULASI PELEBURAN (LEVEL 0 ke LEVEL 1) ---
    # Asumsi resep game: 5 Ore = 1 Ingot/Gems matang
    smelted_silver = ore_silver // 5
    sisa_ore_silver = ore_silver % 5
    
    smelted_gold = ore_gold // 5
    sisa_ore_gold = ore_gold % 5
    
    smelted_diamond = ore_diamond // 5
    sisa_ore_diamond = ore_diamond % 5
    
    smelted_ruby = ore_ruby // 5
    sisa_ore_ruby = ore_ruby % 5
    
    # Total akumulasi di Level 1 (Inventory awal + Hasil peleburan Lvl 0)
    total_silver_ingot = ing_silver + smelted_silver
    total_gold_ingot = ing_gold + smelted_gold
    total_diamond = gem_diamond + smelted_diamond
    total_ruby = gem_ruby + smelted_ruby

    # --- HITUNG HARGA JUAL JIKA LANGSUNG DIJUAL MENTAH (Tanpa Crafting) ---
    nilai_mentah = (
        (ore_silver * p["silver_ore"]) + (ore_gold * p["gold_ore"]) + 
        (ore_diamond * p["diamond_ore"]) + (ore_ruby * p["ruby_ore"]) +
        (ing_silver * p["silver_ingot"]) + (ing_gold * p["gold_ingot"]) + 
        (gem_diamond * p["diamond"]) + (gem_ruby * p["ruby"]) +
        (comp_wire * p["silver_wire"]) + (comp_chain * p["gold_chain"])
    )

    # --- PROSES CRAFTING PERHIASAN (LEVEL 1 & 2 ke LEVEL 3) ---
    # Resep Ring: 1 Silver Ingot + 1 Diamond (Komponen Lvl 2 otomatis dibuat & dirakit)
    crafted_rings = min(total_silver_ingot, total_diamond)
    akhir_silver = total_silver_ingot - crafted_rings
    akhir_diamond = total_diamond - crafted_rings
    
    # Resep Necklace: 1 Gold Ingot + 1 Ruby
    crafted_necklaces = min(total_gold_ingot, total_ruby)
    akhir_gold = total_gold_ingot - crafted_necklaces
    akhir_ruby = total_ruby - crafted_necklaces

    # --- HITUNG TOTAL NILAI JUAL SETELAH OPTIMASI AI ---
    nilai_optimal = (
        (crafted_rings * p["silver_diamond_ring"]) + 
        (crafted_necklaces * p["gold_ruby_necklace"]) +
        # Ditambah sisa bahan yang terpaksa dijual eceran karena kekurangan pasangan:
        (sisa_ore_silver * p["silver_ore"]) + (sisa_ore_gold * p["gold_ore"]) +
        (sisa_ore_diamond * p["diamond_ore"]) + (sisa_ore_ruby * p["ruby_ore"]) +
        (akhir_silver * p["silver_ingot"]) + (akhir_gold * p["gold_ingot"]) +
        (akhir_diamond * p["diamond"]) + (akhir_ruby * p["ruby"]) +
        (comp_wire * p["silver_wire"]) + (comp_chain * p["gold_chain"])
    )
    
    profit_gap = nilai_optimal - nilai_mentah

    # --- GENERATE STRUKTURAL TEKS TERMINAL ---
    report = "🏭 [ALUR PROSES PELEBURAN SMELTER]\n"
    report += "--------------------------------------\n"
    report += f"• Silver Ore di-smelt  : {ore_silver} -> +{smelted_silver} Ingot (Sisa: {sisa_ore_silver} Ore)\n"
    report += f"• Gold Ore di-smelt    : {ore_gold} -> +{smelted_gold} Ingot (Sisa: {sisa_ore_gold} Ore)\n"
    report += f"• Uncut Diamond matang : {ore_diamond} -> +{smelted_diamond} Gem (Sisa: {sisa_ore_diamond} Ore)\n"
    report += f"• Uncut Ruby matang    : {ore_ruby} -> +{smelted_ruby} Gem (Sisa: {sisa_ore_ruby} Ore)\n\n"

    report += "🔨 [REKOMENDASI CRAFTING BENCH (LVL 3)]\n"
    report += "--------------------------------------\n"
    report += f"⚙️ Komponen Lvl 2 dibuat otomatis dari ingot matang.\n"
    report += f"🔥 HASIL AKHIR: Buat {crafted_rings}x Silver Diamond Ring\n"
    report += f"🔥 HASIL AKHIR: Buat {crafted_necklaces}x Gold Ruby Necklace\n\n"

    report += "📦 [SISA LIMPAHAN BAHAN (Dijual Mentah)]\n"
    report += "--------------------------------------\n"
    if akhir_silver: report += f"• {akhir_silver} Silver Ingot matang\n"
    if akhir_gold: report += f"• {akhir_gold} Gold Ingot matang\n"
    if akhir_diamond: report += f"• {akhir_diamond} Diamond Clean\n"
    if akhir_ruby: report += f"• {akhir_ruby} Ruby Clean\n"
    if comp_wire: report += f"• {comp_wire} Silver Wire (Lvl 2 tidak bernilai)\n"
    if comp_chain: report += f"• {comp_chain} Gold Chain (Lvl 2 tidak bernilai)\n"
    
    report += "\n💰 [ANALISIS TOTAL CUAN PASAR]\n"
    report += "--------------------------------------\n"
    report += f"Jika asal Jual Mentah  : Rp {nilai_mentah:,}\n"
    report += f"Jika Lewat AI Optimizer: Rp {nilai_optimal:,}\n"
    report += f"--------------------------------------\n"
    report += f"SELISIH KEUNTUNGAN BERSIH: +Rp {profit_gap:,}\n"

    st.session_state.terminal_output = report
    st.rerun()

if reset:
    st.session_state.terminal_output = "Masukkan data inventory Anda, lalu klik 'Hitung Produksi (AI Optimizer)'..."
    st.rerun()
