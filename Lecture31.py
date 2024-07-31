class Car:
   def __init__(self, model, year, color, for_sale):
       self.model = model
       self.year = year
       self.color = color
       self.for_sale = for_sale

   def drive(self):
       # print("You drive the car")
       # print(f"You drive the {self.model}")
       print(f"You drive the {self.color} {self.model}")

   def stop(self):
       # print("You stop the car")
       # print(f"You stop the {self.model}")
       print(f"You stop the {self.color} {self.model}")

   def describe(self):
       print(f"{self.year} {self.color} {self.model}")
# --------------------------------------

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()
car3.describe()