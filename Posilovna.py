# PROGRAM NA BOLEST NOHOU U DREPU


def hodnoceni_bolavosti (n):
    if n == 1:  return " tak to vážně nemyslíš vážně?"

    elif n >= 2 and n <= 10: return " Budeš mít mírne nepohodlí."

    elif n >=11 and n <=20: return " Možná budeš mít mírně bolavé nohy."

    elif n >=21 and n <=30: return "pomalinku cítíš oheň"

    elif n >=31 and n <=40: return " Invalidita se blíží"

    elif n >=41 and n <=50: return  " mohl by někdo prosím zavolat sanitku?"

# počet provedených dřepu

pocet_drepu = int(input(" Zadej počet provedených dřepu?"))

#  Výpiš hodnocení
print(hodnoceni_bolavosti(pocet_drepu))