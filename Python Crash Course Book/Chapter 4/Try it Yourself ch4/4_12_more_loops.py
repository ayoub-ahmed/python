foods = ('pizza', 'burger', 'pasta', 'salad', 'sushi')
print("\nThe menu is:")
for food in foods:
    print(food)

# Trying to modify a tuple item (this will cause an error)
# foods[0] = 'tacos'

foods = ('pizza', 'tacos', 'pasta', 'rice', 'sushi')

print("\nThe new menu is:")

for food in foods:
    print(food)