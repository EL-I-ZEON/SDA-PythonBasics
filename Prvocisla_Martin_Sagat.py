# Moja zmena pre prvocisla aby neprijala nic len Cisla:


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
    for cislo in range(od, do + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)
            # print(cislo)
    return prvocisla

# Příklad použití


# zmenil som imput na string u oboch imputoch aby bolo mozne zadavat aj pismena bez erroru
od = input("Zadejte počáteční číslo: ")

# zadal som while loop, ak sa zadana hodnota nerovna cislu da hlasku a spyta sa znova
# else statment sluzi k tomu aby som prijatu hodnotu premenil an cislo

while not od.isdigit():
    print("Treba zadat CISLO! ")
    od = input("Zadejte počáteční číslo: ")
else:
    od = int(od)

do = input("Zadejte cislo do: ")

while not do.isdigit():
    print("Vazne to musim opakovat? ")
    do = input("Zadejte cislo do: ")
else:
    do = int(do)

prvocisla = (najdi_prvocisla(od, do))
print(f"Prvočísla v rozmezí {od} až {do} jsou: {prvocisla}")