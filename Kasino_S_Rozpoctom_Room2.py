import random

def kocky():
    while True:
        cisla = set()
        vyhry = []
        vyhra1 = 1000
        vyhra2 = 5000
        rozpocet = 10000

        kocka_1 = random.randint(1, 6)
        kocka_2 = random.randint(1, 6)
        kocka_3 = random.randint(1, 6)

        if cisla.add(kocka_1):
            rozpocet -= 500
            print(f"Rozpocet{rozpocet}")

        cisla.add(kocka_1)
        cisla.add(kocka_2)
        cisla.add(kocka_3)

        if len(cisla) ==1:
            print("Vyhra!")
            vyhry.append(vyhra1 and vyhra2)
            rozpocet -=500
            rozpocet += 5000
        elif len(cisla) >1 and len(cisla)<3:
            print("VVyhra!")
            vyhry.append(vyhra1 and vyhra2)
            rozpocet += 1000
        else:
            print("skus to znova")
            # print(f"{cisla}")
            print(f"{kocka_1} {kocka_2} {kocka_3}")

        x = input(f"Chces to skusit znova? Zadajte Y/N")

        while x not in ["Y", "N"]:
            print("Neplatny vstup použite iba Y/N")
            x = input(f"Chces to skusit znova? Zadajte Y/N")

        if x == ("N"):
            print(f"Dakujeme za hru. Vasa vyhra je {vyhry}")
            break

        print(f"Rozpocet{rozpocet}")

kocky()