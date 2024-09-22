# for Mac
import tkinter as tk
from tkinter import messagebox
class PaymentCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulátor plateb podle položek")
        # Ceník položek
        self.cenik = {"pivo": 3, "kofola": 2, "pizza": 12, "polievka": 1}
        # Vstupy pro počet lidí
        tk.Label(root, text="Kolik lidí se účastní platby?").grid(row=0, column=0)
        self.lidi_input = tk.Entry(root)
        self.lidi_input.grid(row=0, column=1)
        # Tlačítko pro potvrzení počtu lidí
        set_people_button = tk.Button(root, text="Nastavit počet lidí", command=self.create_order_inputs)
        set_people_button.grid(row=1, column=0, columnspan=2)
        # Vstup pro spropitné
        tk.Label(root, text="Spropitné (%)?").grid(row=2, column=0)
        self.spropitne_input = tk.Entry(root)
        self.spropitne_input.grid(row=2, column=1)
        # Tlačítko pro výpočet
        calculate_button = tk.Button(root, text="Vypočítat", command=self.calculate_payment)
        calculate_button.grid(row=3, column=0, columnspan=2)
        # Tabulka pro zobrazení výsledků
        self.result_table = tk.Text(root, height=10, width=50, bg="white", fg="black", font=("Arial", 10))
        self.result_table.grid(row=4, column=0, columnspan=2)
        # Label pro celkový výsledek
        self.result_label = tk.Label(root, text="Celková částka bude zobrazena zde.")
        self.result_label.grid(row=5, column=0, columnspan=2)
        # Pole pro vstupy objednávek
        self.order_inputs = []
    def create_order_inputs(self):
        """Vytvoří vstupy pro objednávky každé osoby podle počtu lidí."""
        try:
            lidi = int(self.lidi_input.get())
            self.order_inputs.clear()
            # Odstranění starých vstupů
            for widget in self.root.grid_slaves():
                if int(widget.grid_info()["row"]) >= 6:
                    widget.grid_forget()
            # Vytváření nových vstupů pro každou osobu
            for i in range(1, lidi + 1):
                tk.Label(self.root, text=f"Osoba {i}:").grid(row=5 + i, column=0)
                pivo_entry = tk.Entry(self.root, width=5)
                kofola_entry = tk.Entry(self.root, width=5)
                pizza_entry = tk.Entry(self.root, width=5)
                polievka_entry = tk.Entry(self.root, width=5)
                pivo_entry.grid(row=5 + i, column=1)
                kofola_entry.grid(row=5 + i, column=2)
                pizza_entry.grid(row=5 + i, column=3)
                polievka_entry.grid(row=5 + i, column=4)
                # Uložení vstupů do seznamu
                self.order_inputs.append({
                    "pivo": pivo_entry,
                    "kofola": kofola_entry,
                    "pizza": pizza_entry,
                    "polievka": polievka_entry
                })
            # Nastavení nadpisů pro vstupy
            tk.Label(self.root, text="Pivo").grid(row=5, column=1)
            tk.Label(self.root, text="Kofola").grid(row=5, column=2)
            tk.Label(self.root, text="Pizza").grid(row=5, column=3)
            tk.Label(self.root, text="Polievka").grid(row=5, column=4)
        except ValueError:
            messagebox.showerror("Chyba", "Zadejte platný počet lidí.")
    def calculate_payment(self):
        try:
            lidi = int(self.lidi_input.get())
            spropitne = int(self.spropitne_input.get()) if self.spropitne_input.get() else 0
            celkova_cena = 0
            # Vymazání výsledků předchozích výpočtů
            self.result_table.delete(1.0, tk.END)
            # Výpočet pro každou osobu
            for i, order in enumerate(self.order_inputs):
                piva = int(order["pivo"].get()) if order["pivo"].get() else 0
                kofola = int(order["kofola"].get()) if order["kofola"].get() else 0
                pizza = int(order["pizza"].get()) if order["pizza"].get() else 0
                polievka = int(order["polievka"].get()) if order["polievka"].get() else 0
                # Výpočet částky pro každou osobu
                castka = (piva * self.cenik["pivo"] +
                          kofola * self.cenik["kofola"] +
                          pizza * self.cenik["pizza"] +
                          polievka * self.cenik["polievka"])
                celkova_cena += castka
                # Zobrazení částky pro každou osobu
                self.result_table.insert(tk.END, f"Osoba {i + 1} zaplatí bez spropitného: {castka:.2f} €\n")
            # Přidání spropitného
            celkova_cena_spropitne = celkova_cena + (celkova_cena * spropitne / 100)
            # Zobrazení celkové částky
            self.result_label.config(text=f"Celková částka bez spropitného: {celkova_cena:.2f} €\n"
                                          f"Celková částka se spropitným: {celkova_cena_spropitne:.2f} €")
        except ValueError:
            messagebox.showerror("Chyba", "Zadejte platné hodnoty.")
if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentCalculatorApp(root)
    root.mainloop()