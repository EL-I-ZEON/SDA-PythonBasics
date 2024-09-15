# def je_prvocislo(cislo, x,y,i):
#     for x,y,i in range(x, y, i):
#         if cislo % i == 0:
#             return False
#     return True


for x,y,i in range(2, 100, 3):
    if x % i == 0:
        y = x % i +1
