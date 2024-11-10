import random


def kocky():

    rozpocet = 10000
    dve_kocky = 1000
    tri_kocky = 5000

    while True:


        kocka1 = random.randint(1, 6)
        kocka2 = random.randint(1, 6)
        kocka3 = random.randint(1, 6)
        # kocka1 = 4
        # kocka2 = 4
        # kocka3 = 4


        print(f"Hádžem prvou kockou a číslo je {kocka1}\n"
              f"Hádžem druhou kockou a číslo je {kocka2}\n"
              f"Hádžem treťou kockou a číslo je {kocka3}\n")

        if kocka1==kocka2==kocka3:
            print(f"Vyhrali ste {tri_kocky}!!!\n"
                  f"Gratulujeme!")
            rozpocet += tri_kocky - 500
            # rozpocet -= 500
            print(f"Váš rozpočet je {rozpocet}")
        elif kocka1 == kocka2 or kocka1 == kocka3 or kocka2 == kocka3:
            print(f"Vyhrali ste {dve_kocky}!!!\n"
                  f"Gratulujeme!")
            rozpocet += dve_kocky - 500
            # rozpocet -= 500
            print(f"Váš rozpočet je {rozpocet}")
        else:
            print("Nevyhrali ste")
            rozpocet -= 500
            print(f"Váš rozpočet je {rozpocet}")


        if rozpocet == 0:
            print("Zbankrotovali ste")
            break
        elif rozpocet > 15000:
            print("Máš šťastný deň, výherca!\n\n")


        m = input(f"Chcete to skúsiť znova?\n\n"
                  f"Zadajte Y/N\n").strip().upper()

        while m not in ["Y", "N"]:
            print("Neplatný vstup. Zadajte Y pre áno alebo N pre nie.")
            m = input("Chcete to skúsiť znova? Zadajte Y/N\n").strip().upper()

        if m == "N":
            print(f"Ďakujeme za hru. Dovidenia!, Vaša celková výhra je {rozpocet}")
            break


kocky()