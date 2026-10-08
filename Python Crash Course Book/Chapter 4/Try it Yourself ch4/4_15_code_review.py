# 4-15. Code Review
# Review your programs from this chapter and make sure they follow PEP 8 guidelines.
# Choose three programs and make any necessary improvements.


# Example 1: Pizzas

pizzas = ["pepperoni", "Neapolitan", "New York"]

print("My favorite pizzas:")

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("\n--------------------")


# Example 2: Odd Numbers

print("Odd numbers:")

for number in range(1, 21, 2):
    print(number)

print("\n--------------------")


# Example 3: Buffet

foods = ("pizza", "burger", "pasta", "salad", "sushi")

print("Buffet menu:")

for food in foods:
    print(food)
