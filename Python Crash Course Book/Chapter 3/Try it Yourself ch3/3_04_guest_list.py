# 3-5. Changing Guest List
# Replace a guest who cannot make it and send new invitations.

guests = ["Albert Einstein","Tim Berners-Lee","Linus Torvalds"]
# Inform everyone that one guest cannot make it.
print(f"{guests[1]} cannot make it to dinner.")

# Replace the unavailable guest.
guests[1] = "Ada Lovelace"

# Print the new invitation messages.
print(f"Dear {guests[0]}, I would like to invite you to dinner.")
print(f"Dear {guests[1]}, I would like to invite you to dinner.")
print(f"Dear {guests[2]}, I would like to invite you to dinner.")