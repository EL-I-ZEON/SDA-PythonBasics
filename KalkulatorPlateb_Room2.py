# Po obede o 13 sa rozhodime nahodne do 4 miestnosti, a dame si spolocnu ulohu:
# Naprogramovat v Pythone:
# Výtejte v kalkuratoru plateb
# zadejte částku kolik máte zaplatit? 100
# Kolik chcete dát spropitného v procentech? 50
# Mezi kolik lidí se má rozdělit částká? 3
# vaše platba je: 50.00 Kč

print("Vitejte v kalkulatoru")
#zadaj sumu
kalkulator_plateb = float(input("Zadej částku v €: "))

#zadaj sprepitné v %
sprepitne = int(input("Zadejte dýško v '%':"))

#sčítanie suma + %
celkova_suma = kalkulator_plateb + ((kalkulator_plateb * sprepitne) / 100)
print("Celkova suma s dýškem" ,celkova_suma, "€")

#delenie medzi osobami
delenie = (celkova_suma  / int(input("Zadej počet osob: ")))
print("Celková suma pro 1 osobu je:", delenie , '€')
