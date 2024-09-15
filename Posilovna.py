# PROGRAM NA BOLEST NOHOU U DREPU


def hodnoceni_bolavosti(n):
    if n == 1:  return " tak to vážně nemyslíš vážně?"

    if n >= 2 and n <= 10: return " Budeš mít mírne nepohodlí."

    if n >= 11 and n <= 20: return " Možná budeš mít mírně bolavé nohy."

    if n >= 21 and n <= 30: return "pomalinku cítíš oheň"

    if n >= 31 and n <= 40: return " Invalidita se blíží"

    if n >= 41 and n <= 50:
        return " mohl by někdo prosím zavolat sanitku?"

    elif n >= 51:
        return "zavolejte pohřebáky"
    else:
        return "kup si permanentku"


# počet provedených dřepu

pocet_drepu = int(input(" Zadej počet provedených dřepu?"))

#  Výpiš hodnocení
print(hodnoceni_bolavosti(pocet_drepu))
