def je_prvocislo(cislo):
    number =[n for n in range(2,10000000)]
    if cislo == 2:
        return True
    if cislo % 2 == 0:
        return False
    for n in number:
        if n == cislo:
            continue
        if cislo % n == 0:
            return False
    else:
        return True
print(je_prvocislo(11))