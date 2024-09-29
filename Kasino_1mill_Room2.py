import random

while True:
    def kocky():

        cisla = set()
        vyhry = []
        vyhra = 1000000

        kocka_1 = random.randint(1, 6)
        kocka_2 = random.randint(1, 6)
        kocka_3 = random.randint(1, 6)

        cisla.add(kocka_1)
        cisla.add(kocka_2)
        cisla.add(kocka_3)

        if len(cisla) ==1:
            print(f"{kocka_1} {kocka_2} {kocka_3}")
            print("VVyhra!")
            vyhry.append(vyhra)
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


kocky()


# import random
#
# def kocky():
#
#     cisla = set()
#
#     kocka_1 = random.randint(1, 6)
#     kocka_2 = random.randint(1, 6)
#     kocka_3 = random.randint(1, 6)
#
#     cisla.add(kocka_1)
#     cisla.add(kocka_2)
#     cisla.add(kocka_3)
#
#     if len(cisla) >1:
#         print("Prehral si")
#     else:
#         print("VVyhra!")
#
#     # print(f"{cisla}")
#     print(f"{kocka_1} {kocka_2} {kocka_3}")

kocky()

# import random
#
#
# def kocky():
#
#     kocka_1 = random.randint(1, 6)
#     kocka_2 = random.randint(1, 6)
#     kocka_3 = random.randint(1, 6)
#
#
#     if kocka_1 == kocka_2 == kocka_3 == 6:
#         print("Vyhra")
#     else:
#         print("Prehra")
#
#     # print(f"{cisla}")
#     print(f"{kocka_1} {kocka_2} {kocka_3}")
#
# kocky()