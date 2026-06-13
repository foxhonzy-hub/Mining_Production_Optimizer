import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

# Set tema visual mirip di video (Dark Mode)
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MiningOptimizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mining Production Optimizer - IME Roleplay")
        self.geometry("700x550")
        self.resizable(False, False)

        # DEFAULTS HARGA PASAR (Bisa diedit di UI)
        self.prices = {
            "silver_ingot": 150,
            "gold_ingot": 300,
            "diamond": 500,
            "ruby": 400,
            "silver_diamond_ring": 1200,
            "gold_ruby_necklace": 1500
        }

        # Variabel untuk Input Inventory
        self.inv_silver = tk.StringVar(value="0")
        self.inv_gold = tk.StringVar(value="0")
        self.inv_diamond = tk.StringVar(value="0")
        self.inv_ruby = tk.StringVar(value="0")

        self.create_widgets()

    def create_widgets(self):
        # ---- TITLE ----
        title_label = ctk.CTkLabel(self, text="MINING PRODUCTION OPTIMIZER", font=ctk.CTkFont(size=22, weight="bold"))
        title_label.pack(pady=15)

        # ---- MAIN FRAME (Split Left & Right) ----
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # LEFT FRAME: INPUT INVENTORY
        left_frame = ctk.CTkScrollableFrame(main_frame, width=300, label_text="Inventory Bahan (Level 1)")
        left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.create_input_field(left_frame, "Silver Ingot:", self.inv_silver)
        self.create_input_field(left_frame, "Gold Ingot:", self.inv_gold)
        self.create_input_field(left_frame, "Diamond:", self.inv_diamond)
        self.create_input_field(left_frame, "Ruby:", self.inv_ruby)

        # Editor Harga Singkat
        price_label = ctk.CTkLabel(left_frame, text="Editor Harga Pasar (NPC)", font=ctk.CTkFont(weight="bold"))
        price_label.pack(pady=(15, 5))
        
        self.price_entries = {}
        for item, price in self.prices.items():
            frame = ctk.CTkFrame(left_frame, fg_color="transparent")
            frame.pack(fill="x", pady=2)
            lbl = ctk.CTkLabel(frame, text=f"{item.replace('_', ' ').title()}:", font=ctk.CTkFont(size=11))
            lbl.pack(side="left")
            ent = ctk.CTkEntry(frame, width=70, height=22)
            ent.insert(0, str(price))
            ent.pack(side="right")
            self.price_entries[item] = ent

        # RIGHT FRAME: HASIL KALKULASI
        right_frame = ctk.CTkFrame(main_frame, width=320)
        right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(right_frame, text="Hasil Optimal Profit", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

        # Output Box
        self.result_text = ctk.CTkTextbox(right_frame, width=300, height=280, font=ctk.CTkFont(size=12))
        self.result_text.pack(pady=5, padx=10)
        self.result_text.insert("0.0", "Masukkan inventory lalu klik 'Hitung Produksi'...")
        self.result_text.configure(state="disabled")

        # ACTION BUTTONS
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(fill="x", side="bottom", pady=15, padx=20)

        calc_btn = ctk.CTkButton(btn_frame, text="Hitung Produksi (AI Optimizer)", command=self.calculate_optimization, fg_color="#2ecc71", hover_color="#27ae60", text_color="black", font=ctk.CTkFont(weight="bold"))
        calc_btn.pack(side="left", expand=True, fill="x", padx=5)

        reset_btn = ctk.CTkButton(btn_frame, text="Reset Input", command=self.reset_inputs, fg_color="#e74c3c", hover_color="#c0392b")
        reset_btn.pack(side="right", expand=True, fill="x", padx=5)

    def create_input_field(self, parent, label_text, variable):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=5)
        label = ctk.CTkLabel(frame, text=label_text, width=120, anchor="w")
        label.pack(side="left")
        entry = ctk.CTkEntry(frame, textvariable=variable, width=100)
        entry.pack(side="right")

    def update_prices_from_ui(self):
        try:
            for item in self.prices:
                self.prices[item] = int(self.price_entries[item].get())
        except ValueError:
            messagebox.showerror("Error", "Harga pasar harus berupa angka bulat!")

    def calculate_optimization(self):
        self.update_prices_from_ui()
        
        try:
            silvers = int(self.inv_silver.get())
            golds = int(self.inv_gold.get())
            diamonds = int(self.inv_diamond.get())
            rubies = int(self.inv_ruby.get())
        except ValueError:
            messagebox.showerror("Error", "Jumlah inventory harus berupa angka!")
            return

        # 1. Hitung Nilai jika Dijual Mentah (Level 1)
        nilai_mentah = (silvers * self.prices["silver_ingot"] +
                        golds * self.prices["gold_ingot"] +
                        diamonds * self.prices["diamond"] +
                        rubies * self.prices["ruby"])

        # 2. Proses Optimizer Kerajinan Perhiasan (Level 3)
        # Bikin Silver Diamond Ring
        crafted_rings = min(silvers, diamonds)
        sisa_silver = silvers - crafted_rings
        sisa_diamond = diamonds - crafted_rings

        # Bikin Gold Ruby Necklace
        crafted_necklaces = min(golds, rubies)
        sisa_gold = golds - crafted_necklaces
        sisa_ruby = rubies - crafted_necklaces

        # 3. Hitung Total Nilai Setelah Optimasi (Perhiasan + Sisa Bahan Mentah)
        nilai_optimal = (crafted_rings * self.prices["silver_diamond_ring"] +
                         crafted_necklaces * self.prices["gold_ruby_necklace"] +
                         sisa_silver * self.prices["silver_ingot"] +
                         sisa_gold * self.prices["gold_ingot"] +
                         sisa_diamond * self.prices["diamond"] +
                         sisa_ruby * self.prices["ruby"])

        profit_gap = nilai_optimal - nilai_mentah

        # Tampilkan Hasil ke UI Box
        self.result_text.configure(state="normal")
        self.result_text.delete("0.0", "end")
        
        report = f"🔨 REKOMENDASI PRODUKSI:\n"
        report += f"-----------------------------------\n"
        report += f"• Buat {crafted_rings}x Silver Diamond Ring\n"
        report += f"• Buat {crafted_necklaces}x Gold Ruby Necklace\n\n"
        
        report += f"📦 SISA BAHAN (Dijual Mentah):\n"
        if sisa_silver: report += f"• {sisa_silver} Silver Ingot\n"
        if sisa_gold: report += f"• {sisa_gold} Gold Ingot\n"
        if sisa_diamond: report += f"• {sisa_diamond} Diamond\n"
        if sisa_ruby: report += f"• {sisa_ruby} Ruby\n"
        if not any([sisa_silver, sisa_gold, sisa_diamond, sisa_ruby]):
            report += "• Tidak ada sisa bahan baku!\n"
            
        report += f"\n💰 PERBANDINGAN CUAN:\n"
        report += f"-----------------------------------\n"
        report += f"Harga Jual Mentah : Rp {nilai_mentah:,}\n"
        report += f"Harga Jual Optimal: Rp {nilai_optimal:,}\n"
        report += f"Selisih Keuntungan: +Rp {profit_gap:,}\n"
        
        self.result_text.insert("0.0", report)
        self.result_text.configure(state="disabled")

    def reset_inputs(self):
        self.inv_silver.set("0")
        self.inv_gold.set("0")
        self.inv_diamond.set("0")
        self.inv_ruby.set("0")
        self.result_text.configure(state="normal")
        self.result_text.delete("0.0", "end")
        self.result_text.insert("0.0", "Masukkan inventory lalu klik 'Hitung Produksi'...")
        self.result_text.configure(state="disabled")

if __name__ == "__main__":
    app = MiningOptimizerApp()
    app.mainloop()
