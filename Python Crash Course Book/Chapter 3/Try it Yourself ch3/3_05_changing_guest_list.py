# 3-6. More Guests
# Add more guests to the dinner list using insert() and append().

guests = ["Albert Einstein","Ada Lovelace","Linus Torvalds"]

print("I found a bigger dinner table!")

# Add a guest to the beginning of the list.
guests.insert(0, "Nikola Tesla")

# Add a guest to the middle of the list.
guests.insert(2, "Alan Turing")

# Add a guest to the end of the list.
guests.append("Guido van Rossum")

# Print invitation messages.
print(f"Dear {guests[0]}, I would like to invite you to dinner.")
print(f"Dear {guests[1]}, I would like to invite you to dinner.")
print(f"Dear {guests[2]}, I would like to invite you to dinner.")
print(f"Dear {guests[3]}, I would like to invite you to dinner.")
print(f"Dear {guests[4]}, I would like to invite you to dinner.")
print(f"Dear {guests[5]}, I would like to invite you to dinner.")