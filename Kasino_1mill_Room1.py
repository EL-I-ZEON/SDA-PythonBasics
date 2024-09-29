import random

def kocky():

    celkova_vyhra = 1000000
    hodnota = 0

    while True:
        kocka1 = random.randint(1, 6)
        kocka2 = random.randint(1, 6)
        kocka3 = random.randint(1, 6)

        print(f"Hádžem prvou kockou a číslo je {kocka1}\n"
              f"Hádžem druhou kockou a číslo je {kocka2}\n"
              f"Hádžem treťou kockou a číslo je {kocka3}\n")

        if kocka1==kocka2==kocka3:
            print("Vyhrali ste milion!!!\n"
                  "Gratulujeme!")
            hodnota += celkova_vyhra
        else:
            print("Nevyhrali ste")

        m = input(f"Chcete to skúsiť znova?\n\n"
                  f"Zadajte Y/N\n").strip().upper()

        while m not in ["Y", "N"]:
            print("Neplatný vstup. Zadajte Y pre áno alebo N pre nie.")
            m = input("Chcete to skúsiť znova? Zadajte Y/N\n").strip().upper()

        if m == "N":
            print(f"Ďakujeme za hru. Dovidenia!, Vaša celková výhra je {hodnota}")
            break
kocky()