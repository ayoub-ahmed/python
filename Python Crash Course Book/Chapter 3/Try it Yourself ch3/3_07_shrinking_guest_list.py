# 3-8. Seeing the World
# Practice working with list order and sorting methods.

places = ["Japan","Brazil","Italy","Canada","New Zealand"]

# Print the original list.
print(places)

# Print the list in alphabetical order without changing it.
print(sorted(places))

# Show the list is still in the original order.
print(places)

# Print the list in reverse alphabetical order without changing it.
print(sorted(places, reverse=True))

# Show the list is still in the original order.
print(places)

# Change the order permanently using reverse().
places.reverse()
print(places)

# Change the order back.
places.reverse()
print(places)

# Sort the list alphabetically.
places.sort()
print(places)

# Sort the list in reverse alphabetical order.
places.sort(reverse=True)
print(places)