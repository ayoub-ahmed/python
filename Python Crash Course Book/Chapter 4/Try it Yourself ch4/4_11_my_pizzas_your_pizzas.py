# 4-11. My Pizzas, Your Pizzas
# Make a copy of a pizza list and add a different pizza to each list.

my_pizzas = ["pepperoni", "margherita", "vegetable"]

friend_pizzas = my_pizzas[:]

my_pizzas.append("hawaiian")
friend_pizzas.append("mushroom")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
