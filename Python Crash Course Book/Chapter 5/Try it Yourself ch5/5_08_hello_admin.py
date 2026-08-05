# 5_09_no_users.py

users = ["admin", "User0", "user1"]

if not users:
    print("We need some users.")
else:
    for user in users:
        if user == "admin":
            print("Hello, Admin")
        else:
            print(f"Welcome, {user}")