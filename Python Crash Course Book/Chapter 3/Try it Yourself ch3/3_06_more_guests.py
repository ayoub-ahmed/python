# 3-7. Shrinking Guest List
# Remove guests until only two guests remain.

guests = ["Nikola Tesla","Albert Einstein","Ada Lovelace","Alan Turing","Linus Torvalds","Guido van Rossum"]

print("Unfortunately, I can invite only two people for dinner.")

# Remove guests one at a time using pop().
removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

# Print the two remaining guests.
print(f"{guests[0]}, you are still invited to dinner.")
print(f"{guests[1]}, you are still invited to dinner.")

# Remove the remaining guests.
del guests[0]
del guests[0]

# Show that the list is empty.
print(guests)