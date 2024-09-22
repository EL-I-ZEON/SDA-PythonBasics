# Vytvoří seznam pomocí for cyklu
numbers = []
for i in range(0,1000,1):
    numbers.append(i)

print(len(numbers))  # Vypíše 1000

# Vytvoří seznam pomocí generátorové notace seznamu - list comprehension
numbers = [i for i in range(0,1000,1)]
print(len(numbers))  # Vypíše 1000

# # Vytvoří slovnik pomocí generátorové notace seznamu - dictionary comprehension
keys_and_values = [("Peter M.", 32), ("Natalka C.", 22), ("Jozko Mrkvicka", 25)]
dictionary = {number: letter for (number, letter) in keys_and_values}
print(keys_and_values)
print(dictionary)


numbers = {number for number in range(0, 10+1,2)}
print(numbers)