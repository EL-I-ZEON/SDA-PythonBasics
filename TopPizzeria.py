import math
from Prvocisla_Martin_Sagat import *

polomer_pizze_mala = 10
polomer_pizze_stredna = 16
polomer_pizze_velka = 25

cena_pizza_mala = 6
cena_pizza_stredna = 9
cena_pizza_velka = 12

def pomer_velkosti_k_cene(polomer, cena):
    pi = 3.14
    plocha = math.pi * polomer * polomer
    # return plocha/cena
    return cena/plocha

print(round(pomer_velkosti_k_cene(10,6),2))
print(round(pomer_velkosti_k_cene(16,9),2))
print(round(pomer_velkosti_k_cene(25,12),2))
print("\n")
print(pomer_velkosti_k_cene(polomer_pizze_mala,cena_pizza_mala))
print(pomer_velkosti_k_cene(polomer_pizze_stredna,cena_pizza_stredna))
print(pomer_velkosti_k_cene(polomer_pizze_velka,cena_pizza_velka))
print("\n")
print(round(pomer_velkosti_k_cene(polomer_pizze_mala,cena_pizza_mala)))
print(round(pomer_velkosti_k_cene(polomer_pizze_stredna,cena_pizza_stredna)))
print(round(pomer_velkosti_k_cene(polomer_pizze_velka,cena_pizza_velka)))
print("\n")

# print(je_prvocislo(100))
print(najdi_prvocisla(100,1000))
dir()

