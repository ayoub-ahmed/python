# 5_02_more_conditional_tests.py

# Equality and inequality
car = "Toyota"
print(car.lower() == "toyota")

car = "jeep"
print(car.upper() != "JEEP")


# Numerical comparisons
temp = 22
print(temp == 20)

temp = 20
print(temp != 20)

age = 18
print(age > 15)

battery = 98
print(battery < 100)

wind = 14
print(wind >= 15)

volt = 5
print(volt <= 4)


# and / or
pet = "cat"
print(pet == "dog" or pet == "cat")

pet = "dog"
print(pet == "dog" and pet == "cat")


# in
cars = ["bmw", "audi"]
print("bmw" in cars)


# not in
cars = ["bmw", "audi"]
print("toyota" not in cars)