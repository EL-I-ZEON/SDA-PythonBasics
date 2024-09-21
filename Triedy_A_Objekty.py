# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"<{self.name} ({self.age})>"
#
#
# print(Animal())

# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self.name = name
#         self.age = age
#
#     def __len__(self):
#         return self.age
#
#
# print(len(Animal("Alex", 3)))

class Animal:
    def __init__(self, name="Rex", age=2):
        self._name = name
        self._age = age

    def __add__(self, other):
        return Animal(self._name, self._age + int(other))

    def __str__(self):
        return f"<{self._name} ({self._age})>"

    def __int__(self):
        return self._age

print(Animal)
print(Animal("Alex", 1) + 1)
print(Animal("Alex", 3) + Animal("Milk", 2))