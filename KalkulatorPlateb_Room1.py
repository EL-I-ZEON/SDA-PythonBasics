# Po obede o 13 sa rozhodime nahodne do 4 miestnosti, a dame si spolocnu ulohu:
# Naprogramovat v Pythone:
# Výtejte v kalkuratoru plateb
# zadejte částku kolik máte zaplatit? 100
# Kolik chcete dát spropitného v procentech? 50
# Mezi kolik lidí se má rozdělit částká? 3
# vaše platba je: 50.00 Kč


# print("Vítejte v kalkulátoru plateb")
# platba = float(input("Kolik máme zaplatit?:"))
# dýško = int(input("kolik chcete dát krásce dýško v %?"))
# plátci = int(input("kolik lidí platí?"))
#
# x = (platba + (platba * (dýško/100))) / plátci
# print("každý zaplatí :", (x))


# def kalkulator_plateb():
#     print("Vítejte v kalkulátoru plateb")
#
#     castka = float(input("Zadejte částku, kolik máte zaplatit: "))
#     spropitne_procenta = float(input("Kolik chcete dát dyška v procentech: "))
#     pocet_lidi = int(input("Mezi kolik lidí se má rozdělit částka: "))
#
#     spropitne = castka * (spropitne_procenta / 100)
#     celkova_castka = castka + spropitne
#
#     platba_na_osobu = celkova_castka / pocet_lidi
#
#     print(f"Vaše platba je: {platba_na_osobu:.2f} Kč")
#
#
# print(kalkulator_plateb())

def kalkulator_plateb():
    print("Vítejte v kalkulátoru plateb")

    pocet_lidi = int(input("Kolik lidí šlo na pivko? "))

    objednavky = []
    platby = []

    ceny = {
        "pivo": 3,
        "kofola": 2,
        "pizza": 12,
        "polievka": 1
    }
    for i in range(pocet_lidi):
        print(f"\nOsoba {i + 1}:")
        pivo_pocet = int(input("Kolik jste měl piv? "))
        kofola_pocet = int(input("Kolik jste měl kofol? "))
        pizza_pocet = int(input("Kolik bylo pizz? "))
        polievka_pocet = int(input("Polivčička byla? "))

        objednavky.append({
            "pivo": pivo_pocet,
            "kofola": kofola_pocet,
            "pizza": pizza_pocet,
            "polievka": polievka_pocet
        })
    spropitne_procenta = float(input("\nKolik chcete dát dýška v procentech? "))

# Zde už jsem použil AI
    for objednavka in objednavky:
        celkova_castka = sum(objednavka[item] * ceny[item] for item in objednavka)
        spropitne = celkova_castka * (spropitne_procenta / 100)
        celkova_castka_se_spropitnym = celkova_castka + spropitne
        platby.append(celkova_castka_se_spropitnym)

    for i, platba in enumerate(platby):
        print(f"\nOsoba {i + 1}:")
        print(f"Celková částka bez dýšek je: {platba - (platba * (spropitne_procenta / (100 + spropitne_procenta))):.2f} €")
        print(f"Celková částka s dyškem je: {platba:.2f} €")


kalkulator_plateb()