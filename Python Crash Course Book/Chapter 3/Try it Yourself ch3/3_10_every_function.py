# 3-10. Every Function
# Create a list and use different functions with the list.

languages = ["Python", "Java", "C++", "JavaScript", "Go"]

# Access an item using an index.
print(languages[0])

# Add a new item to the list.
languages.append("Rust")
print(languages)

# Insert an item at a specific position.
languages.insert(1, "C#")
print(languages)

# Remove an item from the list.
languages.remove("Java")
print(languages)

# Sort the list alphabetically.
languages.sort()
print(languages)

# Reverse the order of the list.
languages.reverse()
print(languages)

# Display the number of items in the list.
print(len(languages))