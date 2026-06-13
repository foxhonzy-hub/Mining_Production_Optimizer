import streamlit as st

# Pengaturan Konfigurasi Halaman Web
st.set_page_config(
    page_title="Mining Production Optimizer - IME Roleplay",
    page_icon="⛏️",
    layout="centered"
)

st.title("⛏️ Mining Production Optimizer")
st.subheader("IME Roleplay Server Tools")
st.write("Optimalkan hasil tambangmu untuk mendapatkan cuan maksimal dari NPC/Pemerintah!")

st.divider()

# DEFAULTS HARGA PASAR (Bisa diedit di web)
if "prices" not in st.session_state:
    st.session_state.prices = {
        "silver_ingot": 150,
        "gold_ingot": 300,
        "diamond": 500,
        "ruby": 400,
        "silver_diamond_ring": 1200,
        "gold_ruby_necklace": 1500
    }

# MEMBUAT KOLOM INPUT (Kiri: Inventory, Kanan: Editor Harga)
col1, col2 = st.columns(2)

with col1:
    st.header("📦 Inventory Bahan (Lvl 1)")
    inv_silver = st.number_input("Jumlah Silver Ingot", min_value=0, value=0, step=1)
    inv_gold = st.number_input("Jumlah Gold Ingot", min_value=0, value=0, step=1)
    inv_diamond = st.number_input("Jumlah Diamond", min_value=0, value=0, step=1)
    inv_ruby = st.number_input("Jumlah Ruby", min_value=0, value=0, step=1)

with col2:
    st.header("💰 Editor Harga NPC")
    for item in st.session_state.prices.keys():
        clean_name = item.replace("_", " ").title()
        st.session_state.prices[item] = st.number_input(
            f"Harga {clean_name}", 
            min_value=0, 
            value=st.session_state.prices[item], 
            step=10
        )

st.divider()

# TOMBOL HITUNG
if st.button("🚀 HITUNG PRODUKSI OPTIMAL", type="primary", use_container_width=True):
    prices = st.session_state.prices
    
    # 1. Hitung Nilai jika Dijual Mentah
    nilai_mentah = (inv_silver * prices["silver_ingot"] +
                    inv_gold * prices["gold_ingot"] +
                    inv_diamond * prices["diamond"] +
                    inv_ruby * prices["ruby"])

    # 2. Proses Optimizer Kerajinan Perhiasan (Level 3)
    # Bikin Silver Diamond Ring (1 Silver + 1 Diamond)
    crafted_rings = min(inv_silver, inv_diamond)
    sisa_silver = inv_silver - crafted_rings
    sisa_diamond = inv_diamond - crafted_rings

    # Bikin Gold Ruby Necklace (1 Gold + 1 Ruby)
    crafted_necklaces = min(inv_gold, inv_ruby)
    sisa_gold = inv_gold - crafted_necklaces
    sisa_ruby = inv_ruby - crafted_necklaces

    # 3. Hitung Total Nilai Setelah Optimasi
    nilai_optimal = (crafted_rings * prices["silver_diamond_ring"] +
                     crafted_necklaces * prices["gold_ruby_necklace"] +
                     sisa_silver * prices["silver_ingot"] +
                     sisa_gold * prices["gold_ingot"] +
                     sisa_diamond * prices["diamond"] +
                     sisa_ruby * prices["ruby"])

    profit_gap = nilai_optimal - nilai_mentah

    # TAMPILKAN HASIL DI WEBSITE
    st.header("📊 Hasil Analisis AI Optimizer")
    
    # Kolom Output
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.subheader("🔨 Rekomendasi Crafting")
        st.success(f"**{crafted_rings}x** Silver Diamond Ring")
        st.success(f"**{crafted_necklaces}x** Gold Ruby Necklace")
        
        st.caption("Sisa bahan mentah untuk dijual langsung:")
        if sisa_silver: st.write(f"• {sisa_silver} Silver Ingot")
        if sisa_gold: st.write(f"• {sisa_gold} Gold Ingot")
        if sisa_diamond: st.write(f"• {sisa_diamond} Diamond")
        if sisa_ruby: st.write(f"• {sisa_ruby} Ruby")
        if not any([sisa_silver, sisa_gold, sisa_diamond, sisa_ruby]):
            st.write("• Tidak ada sisa, semua bahan terpakai sempurna!")

    with res_col2:
        st.subheader("💵 Perbandingan Cuan")
        st.info(f"**Jual Mentah:** Rp {nilai_mentah:,}")
        st.info(f"**Jual Hasil Optimasi:** Rp {nilai_optimal:,}")
        
        if profit_gap > 0:
            st.warning(f"📈 **Tambahan Keuntungan:** +Rp {profit_gap:,}")
        else:
            st.write("ℹ️ Hasil penjualan mentah dan crafting sama saja.")
