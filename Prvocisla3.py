def je_prvocislo(cislo):
    if cislo == 2:
        return True
    if cislo < 2 or cislo % 2 == 0:
        return False
    for n in range(3, int(cislo ** 0.5) + 1, 2):
        if cislo % n == 0:
            return False
    return True


def najdi_prvocisla(od, do):
    prvocisla = []
    while od & do != int:
        od = int(input("CHYBA - Zadejte počáteční číslo: "))
        do = int(input("CHYBA - Zadejte číslo do: "))
    if od & do == int:
        for cislo in range(od, do + 1):
            if je_prvocislo(cislo):
                prvocisla.append(cislo)
                # print(cislo)
        return prvocisla


# Příklad použití
od = int(input("Zadejte počáteční číslo: "))
do = int(input("Zadejte číslo do: "))

prvocisla = najdi_prvocisla(od, do)
print(f"Prvočísla v rozmezí {od} až {do} jsou: {prvocisla}")
