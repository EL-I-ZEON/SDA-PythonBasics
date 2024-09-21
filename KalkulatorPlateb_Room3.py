# Po obede o 13 sa rozhodime nahodne do 4 miestnosti, a dame si spolocnu ulohu:
# Naprogramovat v Pythone:
# Výtejte v kalkuratoru plateb
# zadejte částku kolik máte zaplatit? 100
# Kolik chcete dát spropitného v procentech? 50
# Mezi kolik lidí se má rozdělit částká? 3
# vaše platba je: 50.00 Kč

print("Výtejte v kalkulatoru plateb")
cena = float(input("Kolik mate zaplatit? "))
spropitne = int(input("kolik chcete dat spropitnehov(%) "))
lidi= int(input("mezi kolik lidi rozdělit platbu "))

jedna_cena =(cena + ( cena * spropitne / 100 )) / lidi

print(f" Každy šlovek zaplati {jedna_cena} kč")
