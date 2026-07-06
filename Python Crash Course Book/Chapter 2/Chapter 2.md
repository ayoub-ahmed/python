
# Variables and Simple Data Types

## 1. Overview
In this chapter, you learn:
- How Python stores and handles data
- What variables are and how they work
- Basic data types (strings and numbers)
- Common errors and how to avoid them

---

## 2. What Happens When You Run `hello_world.py`
When you run:

```python id="c1a8x9"
print("Hello Python world!")
````

Python:

1. Reads the `.py` file
    
2. Interprets the code line by line
    
3. Recognizes `print()` as a function
    
4. Displays the text inside parentheses
    

---

## 3. Variables

### What is a Variable?

A variable is a label that stores a value in memory.

```python
message = "Hello Python world!"
print(message)
```

Output:

```text
Hello Python world!
```

---

### Updating Variables

Variables can change value:

```python
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```

---

## 4. Naming Rules for Variables

Rules:

- Must contain letters, numbers, underscores
    
- Cannot start with a number
    
- No spaces allowed
    
- Cannot use Python keywords (e.g., `print`)
    

Good practice:

- `student_name` ✔
    
- `name` ✔
    
- `s_n` (less clear)
    

---

## 5. Common Errors

### Name Error

Occurs when variable is misspelled:

```python
message = "Hello"
print(mesage)
```

Python output:

- `NameError: name is not defined`
    

👉 Python is case-sensitive and spelling-sensitive

---

## 6. Variables Are Labels (Not Boxes)

- Variables do NOT store values like boxes
    
- They are **labels pointing to values**
    

---

## 7. Try It Yourself (IMPORTANT)

### 2-1 Simple Message

- Create a variable
    
- Print it
    

---

### 2-2 Simple Messages

- Create variable
    
- Print it
    
- Change value
    
- Print again
    

---

## 8. Strings

### What is a String?

A string is text inside quotes:

```python
"Hello"
'Hello'
```

---

## 9. String Methods

### Change Case

```python
name = "ada lovelace"
print(name.title())
```

Output:

```
Ada Lovelace
```

Other methods:

```python
print(name.upper())
print(name.lower())
```

---

## 10. f-Strings (Formatted Strings)

```python
first = "ada"
last = "lovelace"

full = f"{first} {last}"
print(full)
```

Output:

```
ada lovelace
```

---

## 11. Whitespace in Strings

### Tabs and Newlines

```python
print("Languages:\nPython\nC\nJava")
```

Output:

```
Languages:
Python
C
Java
```

---

## 12. Stripping Whitespace

```python
name = " python "
print(name.strip())
```

Methods:

- `rstrip()` → right side
    
- `lstrip()` → left side
    
- `strip()` → both sides
    

---

## 13. Numbers in Python

### Integers

```python
2 + 3
3 * 4
10 / 2
```

---

### Floats (decimals)

```python
0.1 + 0.2
```

Note: floating-point precision errors may occur.

---

### Exponents

```python
3 ** 2
```

---

### Underscores for readability

```python
universe_age = 14_000_000_000
```

---

## 14. Multiple Assignment

```python
x, y, z = 0, 0, 0
```

---

## 15. Constants

Convention:

```python
MAX_CONNECTIONS = 5000
```

(All caps = treat as constant)

---

## 16. Comments

```python
# This is a comment
print("Hello")
```

Purpose:

- Explain code
    
- Improve readability
    
- Help future you
    

---

## 17. Try It Yourself (IMPORTANT)

### 2-3 Personal Message

- Print greeting to a person
    

### 2-4 Name Cases

- lowercase
    
- uppercase
    
- title case
    

### 2-5 Famous Quote

- Print quote with author
    

### 2-6 Famous Quote 2

- Use variables for quote + author
    

### 2-7 Stripping Names

- Use whitespace + strip methods
    

---

## 18. Zen of Python

Run:

```python
import this
```

Key ideas:

- Simple is better than complex
    
- Readability matters
    
- Keep code clean and clear
    

---

## 19. Summary

You learned:

- Variables and how they work
    
- Strings and string methods
    
- Numbers (int, float, operations)
    
- Comments
    
- Basic debugging
    
- Python philosophy (Zen of Python)
    

---

## References

[1] Python Crash Course — Chapter 2
