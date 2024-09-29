import random

def hod_kostkou():
    return random.randint(1, 6)

def hod_tri_kostek():

    kostka1 = hod_kostkou()
    kostka2 = hod_kostkou()
    kostka3 = hod_kostkou()

    print(f"Hod kostky 1: {kostka1}")
    print(f"Hod kostky 2: {kostka2}")
    print(f"Hod kostky 2: {kostka3}")
    print(f"Součet hodů: {kostka1 + kostka2 + kostka3}")

    if  kostka1 == kostka2 == kostka3 == 6:
        print("vyhrali jste 5 milionu")
    elif kostka1 == kostka2 == kostka3==2:
        print("Vyhráli jste 1 milion!")
    elif kostka1 == kostka2 == kostka3==4:
        print("Vyhráli jste 2 miliony!")
    else:
        print(" Maš smulu")

hod_tri_kostek()