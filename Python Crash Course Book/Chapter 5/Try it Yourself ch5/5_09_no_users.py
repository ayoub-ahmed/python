# 5_10_checking_usernames.py

current_users = ["user0", "User1", "user2", "USER3", "user4"]
new_users = ["user1", "user5", "USER2", "user6", "User4"]

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"'{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"'{new_user}' is available.")