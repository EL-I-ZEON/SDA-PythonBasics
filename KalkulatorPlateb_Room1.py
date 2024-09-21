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

def kalkulator_plateb():
    print("Vítejte v kalkulátoru plateb")

    castka = float(input("Zadejte částku, kolik máte zaplatit: "))
    spropitne_procenta = float(input("Kolik chcete dát dyška v procentech: "))
    pocet_lidi = int(input("Mezi kolik lidí se má rozdělit částka: "))

    spropitne = castka * (spropitne_procenta / 100)
    celkova_castka = castka + spropitne

    platba_na_osobu = celkova_castka / pocet_lidi

    print(f"Vaše platba je: {platba_na_osobu:.2f} Kč")


print(kalkulator_plateb())