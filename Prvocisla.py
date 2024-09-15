import math

# ma_zvysok = 13 % 2
# print(ma_zvysok)


def je_prvocislo(cislo):
    print(f"Nase cislo je {cislo}")
    rozsah = int((math.sqrt(cislo)))
    # rozsah = [i for i in range(2, delitel+1)]
    # print(f"Nas rozsah je {rozsah}")
    print(f"Nas rozsah je {rozsah}")
    if cislo == 2:
        print(f"{cislo} je prvocislo")
        return True
    for delitel in range(2, rozsah+1, 2):
        # print(f"Pokus s cislom {n}")
        if cislo % delitel == 0:
            print(f"{cislo} nie je prvocislo")
            return False
    else:
        print(f"{cislo} je prvocislo")
        return True

print(je_prvocislo(2),"\n")
print(je_prvocislo(3),"\n")
print(je_prvocislo(4),"\n")
print(je_prvocislo(5),"\n")
print(je_prvocislo(6),"\n")
print(je_prvocislo(7),"\n")
print(je_prvocislo(9),"\n")
print(je_prvocislo(11),"\n")
print(je_prvocislo(13),"\n")
print(je_prvocislo(17),"\n")
print(je_prvocislo(1000001),"\n")
print(je_prvocislo(1000000181),"\n")
print(je_prvocislo(1000000182),"\n")
print(je_prvocislo(1000000207),"\n")
