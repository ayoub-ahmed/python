pizzas = ['pepperoni', 'Neapolitan', 'New York']

friend_pizzas = pizzas[:]

pizzas.append("pineapple")
friend_pizzas.append("tuna")

print("My favorite pizzas are:")

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("\nMy friend's favorite pizzas are:")

for pizza in friend_pizzas:
    print(f"My friend likes {pizza} pizza.")