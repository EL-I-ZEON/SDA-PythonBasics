alphabet = ['a', 'b', 'c', '...', 'z']

phone_numbers2 = {
    "Jan": 111111111,
    "Karel": 222222222,
    "meno" : "Jan Karel"
}

tupple2 = ("pes", "kočka", 2000, 5.0, True)
tupple3 = ("a", 2, "c", [1, 2, 3], "x", "y", "z")

# print(tupple3[3])
# print(alphabet[4])
# print(phone_numbers2)

# print(tupple3[1:4])

animals = {"pes", "kočka", "slon", 2}
animals.add("myš")

set_1 = {1, 2, 3}
set_2 = {2, 3, 4, 5, "myš", 6}

# print(set_2)
# print(set_1 | set_2 | animals)
# print(animals.union(set_2))
print(set_2.difference(animals))
print(animals.difference(set_2))