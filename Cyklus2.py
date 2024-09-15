n = 0
while n < 5:
    n += 2  # Zvýší n s každým průchodem cyklu (iterací)
    print(n)

animals = ["Pes", "Kočka", "Ryba"]

# Vypíše všechna zvířata ze seznamu zvirata
for animal in animals:
    print(animal)


for number in range(-1, -4, -1):
    print(number)

fruits = ["jablko", "banán", "citrón"]

for index, fruit in enumerate(fruits):
    print(f"Druh ovoce: {fruit}, na indexu: {index}.")