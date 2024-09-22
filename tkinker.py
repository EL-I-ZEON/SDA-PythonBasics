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

        # Vstupy pro počet položek
        tk.Label(root, text="Kolik piv?").grid(row=1, column=0)
        self.pivo_input = tk.Entry(root)
        self.pivo_input.grid(row=1, column=1)

        tk.Label(root, text="Kolik kofol?").grid(row=2, column=0)
        self.kofola_input = tk.Entry(root)
        self.kofola_input.grid(row=2, column=1)

        tk.Label(root, text="Kolik pizz?").grid(row=3, column=0)
        self.pizza_input = tk.Entry(root)
        self.pizza_input.grid(row=3, column=1)

        tk.Label(root, text="Kolik polévek?").grid(row=4, column=0)
        self.polievka_input = tk.Entry(root)
        self.polievka_input.grid(row=4, column=1)

        # Vstup pro spropitné
        tk.Label(root, text="Kolik chcete dát spropitné (%)?").grid(row=5, column=0)
        self.spropitne_input = tk.Entry(root)
        self.spropitne_input.grid(row=5, column=1)

        # Tlačítko pro výpočet
        calculate_button = tk.Button(root, text="Vypočítat", command=self.calculate_payment)
        calculate_button.grid(row=6, column=0, columnspan=2)

        # Label pro výstup výsledku
        self.result_label = tk.Label(root, text="Celková částka bude zobrazena zde.")
        self.result_label.grid(row=7, column=0, columnspan=2)

    def calculate_payment(self):
        try:
            # Získání vstupních hodnot
            lidi = int(self.lidi_input.get())
            piva = int(self.pivo_input.get()) if self.pivo_input.get() else 0
            kofola = int(self.kofola_input.get()) if self.kofola_input.get() else 0
            pizza = int(self.pizza_input.get()) if self.pizza_input.get() else 0
            polievka = int(self.polievka_input.get()) if self.polievka_input.get() else 0
            spropitne = int(self.spropitne_input.get()) if self.spropitne_input.get() else 0

            # Výpočet celkové ceny bez spropitného
            celkova_cena = (piva * self.cenik["pivo"] +
                            kofola * self.cenik["kofola"] +
                            pizza * self.cenik["pizza"] +
                            polievka * self.cenik["polievka"])

            # Přidání spropitného
            celkova_cena_spropitne = celkova_cena + (celkova_cena * spropitne / 100)

            # Aktualizace výstupu
            self.result_label.config(text=f"Celková částka včetně spropitného: {celkova_cena_spropitne:.2f} €")
        except ValueError:
            messagebox.showerror("Chyba", "Zadejte platné hodnoty.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentCalculatorApp(root)
    root.mainloop()
