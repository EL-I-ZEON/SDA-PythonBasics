# Po obede o 13 sa rozhodime nahodne do 4 miestnosti, a dame si spolocnu ulohu:
# Naprogramovat v Pythone:
# Výtejte v kalkuratoru plateb
# zadejte částku kolik máte zaplatit? 100
# Kolik chcete dát spropitného v procentech? 50
# Mezi kolik lidí se má rozdělit částká? 3
# vaše platba je: 50.00 Kč

# print("Výtejte v kalkulatoru plateb")
# cena = float(input("Kolik mate zaplatit? "))
# spropitne = int(input("kolik chcete dat spropitnehov(%) "))
# lidi= int(input("mezi kolik lidi rozdělit platbu "))
#
# jedna_cena =(cena + ( cena * spropitne / 100 )) / lidi
#
# print(f" Každy šlovek zaplati {jedna_cena} kč")





# print("Vítejte v kalkulátoru plateb podle položek")
# cenik = {
#     "pivo": 3,
#     "kofola": 2,
#     "pizza": 12,
#     "polievka": 1
# }
# lidi = int(input("Kolik lidí se účastní platby? "))
# objednavky = {}
# for i in range(1, lidi + 1):
#     print(f"\nOsoba {i}:")
#     pivo = int(input("Kolik piv jste objednali? "))
#     kofola = int(input("Kolik kofol jste objednali? "))
#     pizza = int(input("Kolik pizz jste objednali? "))
#     polievka = int(input("Kolik polévek jste objednali? "))
#     # Vypočítání ceny za každou osobu
#     objednavky[f"Osoba {i}"] = (pivo * cenik["pivo"]) + (kofola * cenik["kofola"]) + (pizza * cenik["pizza"]) + (
#             polievka * cenik["polievka"])
# spropitne = int(input("\nKolik chcete dát spropitné (%)? "))
# celkova_cena = sum(objednavky.values())
# print(f"\nCelková částka bez spropitného: {celkova_cena:.2f} €")
# celkova_cena_spropitne = celkova_cena + (celkova_cena * spropitne / 100)
# print("\nVýsledné částky pro každého:")
# for osoba, castka in objednavky.items():
#     castka_spropitne = castka + (castka * spropitne / 100)
#     print(f"{osoba} zaplatí: {castka_spropitne:.2f} €")
# print(f"\nCelková částka včetně spropitného: {celkova_cena_spropitne:.2f} €")

print("Vítejte v kalkulátoru plateb podle položek")

cenik = {"pivo": 3, "kofola": 2, "pizza": 12, "polievka": 1}

lidi = int(input("Kolik lidí se účastní platby? "))
celkova_cena = 0

for i in range(1, lidi + 1):
    print(f"\nOsoba {i}:")
    objednavka = sum(int(input(f"Kolik {polozka}? ")) * cena for polozka, cena in cenik.items())
    celkova_cena += objednavka
    print(f"Osoba {i} zaplatí bez spropitného: {objednavka:.2f} €")

spropitne = int(input("\nKolik chcete dát spropitné (%)? "))
celkova_cena_spropitne = celkova_cena + (celkova_cena * spropitne / 100)

print(f"\nCelková částka včetně spropitného: {celkova_cena_spropitne:.2f} €")