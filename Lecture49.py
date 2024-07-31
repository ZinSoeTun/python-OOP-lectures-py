# SORTING IN PYTHON .sort() or sorted()
# Lists[], Tuples(), Dictionaries{"":""}, Objects

# ---------- LISTS ----------
fruits = ["banana", "orange", "apple", "coconut"]

# fruits.sort()
# fruits.sort(reverse=True)

print(fruits)

# ---------- TUPLES ----------
fruits = ("banana", "orange", "apple", "coconut")

# fruits = tuple(sorted(fruits))
# fruits = tuple(sorted(fruits, reverse=True))

print(fruits)

# ---------- DICTIONARIES ----------
fruits = {
   "banana": 105,
   "apple": 72,
   "orange": 73,
   "coconut": 354
}

# fruits = dict(sorted(fruits.items()))
# fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))
# fruits = dict(sorted(fruits.items(), key=lambda item: item[1]))
# fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))

print(fruits)

# ---------- OBJECTS ----------
class Fruit:
   def __init__(self, name, calories):
       self.name = name
       self.calories = calories

   def __repr__(self):
       return f"{self.name}: {self.calories}"

fruits = [Fruit("banana", 105),
              Fruit("apple", 72),
              Fruit("orange", 73),
              Fruit("coconut", 354)]

# fruits = sorted(fruits, key=lambda fruit: fruit.name)
# fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
# fruits = sorted(fruits, key=lambda fruit: fruit.calories)
# fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)

print(fruits)