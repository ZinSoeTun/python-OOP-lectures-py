# map(function, collection) = Applies a given function to all items in a collection

celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

fahrenheit_temps = list(map(lambda temp: (temp * 9 / 5) + 32, celsius_temps))

print(fahrenheit_temps)

# filter(condition, collection) = return all elements that pass a condition

grades = [91, 32, 83, 44, 75, 56, 67]

passing_grades = list(filter(lambda grade: grade >= 60, grades))

print(passing_grades)

# reduce(function, collection) = Reduces elements in a collection to a single value
#                                                      For loop is better in most cases
#                                                      Reduce is better for a functional approach + readability

from functools import reduce

prices = [19.99, 1.00, 5.75, 12.99, 10.99]

total = reduce(lambda x, y: x + y, prices)

print(f"${total}")