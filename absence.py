absence = {}
while True:
    student = input("Zadejte jméno studenta (nebo 'konec' pro ukončení): ")
    if student == 'konec': break
    absence[student] = absence.get(student, 0) + int(input(f"Počet dnů absence pro {student}: "))
print(absence)
