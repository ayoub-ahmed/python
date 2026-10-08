# 3-5. Changing Guest List
# Replace a guest who can't attend with a new guest and print the updated invitations.

guests = ["Albert Einstein", "Nikola Tesla", "Alan Turing"]

print(f"Unfortunately, {guests[1]} can't make it to dinner.")

guests[1] = "Marie Curie"

for guest in guests:
    print(f"Hello {guest}, I would like to invite you to dinner.")
