# 3-6. More Guests
# Add more guests to the dinner list and print a new invitation message for each guest.

guests = ["Albert Einstein", "Marie Curie", "Alan Turing"]

guests.insert(0, "Isaac Newton")
guests.insert(2, "Ada Lovelace")
guests.append("Charles Darwin")

for guest in guests:
    print(f"Hello {guest}, I would like to invite you to dinner.")
