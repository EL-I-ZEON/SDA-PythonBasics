import random


def hod_kostkou():
    return random.randint(1, 6)


def hod_tri_kostek():
    rozpočet = 10000
    cena_hodu = 500
    while True:
        if rozpočet < cena_hodu:
            print("Nemáte dostatek peněz na další hod.")
            print("Bankrot!")
            break

        rozpočet -= cena_hodu  # Odečtení ceny za hod
        kostka1 = hod_kostkou()
        kostka2 = hod_kostkou()
        kostka3 = hod_kostkou()

        print(f"Hod kostky 1: {kostka1}")
        print(f"Hod kostky 2: {kostka2}")
        print(f"Hod kostky 3: {kostka3}")
        print(f"Součet hodů: {kostka1 + kostka2 + kostka3}")

        # Vyhodnocení výhry
        if kostka1 == kostka2 == kostka3:
            if kostka1 == 2:
                print("Vyhráli jste 1 000 Kč!")
                rozpočet += 1000  # Přičtení výhry
            elif kostka1 == 6:
                print("Vyhráli jste 5 000 Kč!")
                rozpočet += 5000  # Přičtení výhry
            else:
                print("Vyhráli jste 0 Kč, ale máte tři stejné!")
        else:
            print("Máte smůlu.")

        # Zobrazení aktuálního rozpočtu
        print(f"Váš aktuální rozpočet je: {rozpočet} Kč")

        # Zeptejte se hráče, zda chce hrát dál
        odpoved = input("Chcete hrát dále? ano/ne: ").lower()
        if odpoved != "ano":
            break


hod_tri_kostek()