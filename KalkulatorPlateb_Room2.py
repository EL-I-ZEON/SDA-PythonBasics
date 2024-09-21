# Po obede o 13 sa rozhodime nahodne do 4 miestnosti, a dame si spolocnu ulohu:
# Naprogramovat v Pythone:
# Výtejte v kalkuratoru plateb
# zadejte částku kolik máte zaplatit? 100
# Kolik chcete dát spropitného v procentech? 50
# Mezi kolik lidí se má rozdělit částká? 3
# vaše platba je: 50.00 Kč

# print("Vitejte v kalkulatoru")
# #zadaj sumu
# kalkulator_plateb = float(input("Zadej částku v €: "))
#
# #zadaj sprepitné v %
# sprepitne = int(input("Zadejte dýško v '%':"))
#
# #sčítanie suma + %
# celkova_suma = kalkulator_plateb + ((kalkulator_plateb * sprepitne) / 100)
# print("Celkova suma s dýškem" ,celkova_suma, "€")
#
# #delenie medzi osobami
# delenie = (celkova_suma  / int(input("Zadej počet osob: ")))
# print("Celková suma pro 1 osobu je:", delenie , '€')



# Kalkulátor plateb
print("Vítejte v kalkulátoru plateb!")

# Definice cen položek
ceny = {
    "pivo": 3,
    "kofola": 2,
    "pizza": 12,
    "polevka": 1
}

# Zadat procento spropitného
spropitne_procenta = float(input("Kolik chcete dát spropitného v procentech? "))

# Zadat počet lidí, kteří se podíleli na objednávce
pocet_lidi = int(input("Kolik lidí se účastní rozdělení platby? "))

# Získání objednávek pro každou osobu
objednavky = []

for i in range(1, pocet_lidi + 1):
    print(f"\nObjednávky pro osobu {i}:")
    piva = int(input("Kolik piv? "))
    kofoly = int(input("Kolik kofol? "))
    pizzy = int(input("Kolik pizz? "))
    polevky = int(input("Kolik polévek? "))
    objednavky.append({
        "pivo": piva,
        "kofola": kofoly,
        "pizza": pizzy,
        "polevka": polevky
    })

# Výpočet celkové částky pro každou osobu
platby = []

for objednavka in objednavky:
    platba = (
        objednavka["pivo"] * ceny["pivo"] +
        objednavka["kofola"] * ceny["kofola"] +
        objednavka["pizza"] * ceny["pizza"] +
        objednavka["polevka"] * ceny["polevka"]
    )
    platby.append(platba)

# Celková částka za všechny osoby
celkova_castka = sum(platby)
print(f"\nCelková částka bez spropitniho: {celkova_castka:.2f} €")

# Přidání spropitného
celkova_castka += celkova_castka * (spropitne_procenta / 100)


# Výpočet a výpis platby pro každou osobu
print("\nRozdělení plateb:")
for i, platba in enumerate(platby, 1):
    platba_se_spropitnym = platba + (platba * (spropitne_procenta / 100))
    print(f"Osoba {i} zaplatí: {platba_se_spropitnym:.2f} €")

# Výstup celkové částky
print(f"\nCelková částka se spropitným: {celkova_castka:.2f} €")
