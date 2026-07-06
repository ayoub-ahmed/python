
# Working with Lists

Lists are one of the most important data structures in Python. They allow you to store multiple values and process them efficiently using loops, slicing, and built-in functions.

---

## Looping Through Lists

A `for` loop lets you go through every item in a list automatically.

```python
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)
````

Python repeats the indented block once for every item in the list.

---

## A Closer Look at Looping

Each loop cycle works like this:

1. Take the next item from the list
    
2. Assign it to the loop variable
    
3. Execute the indented block
    
4. Repeat until the list ends
    

Example:

```python
for magician in magicians:
    print(magician)
```

---

## Doing Work in a Loop

You can do more than one action inside a loop:

```python
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

Each indented line runs once per item.

---

## After the Loop

Code that is NOT indented runs once after the loop ends:

```python
for magician in magicians:
    print(magician)

print("Thank you everyone!")
```

---

## Indentation Rules & Errors

Python uses indentation to define structure.

Common mistakes:

- Missing indentation → error
    
- Extra indentation → error
    
- Wrong placement → logic bug
    

Example error:

```python
for magician in magicians:
print(magician)  # wrong
```

---

## range() Function

Generate numbers:

```python
for value in range(1, 6):
    print(value)
```

⚠️ The last number is NOT included.

---

## Numerical Lists

Convert range into a list:

```python
numbers = list(range(1, 6))
```

### Even numbers

```python
even_numbers = list(range(2, 11, 2))
```

### Squares

```python
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
```

---

## List Comprehensions

Short version of loops:

```python
squares = [value**2 for value in range(1, 11)]
```

---

## Slicing Lists

Get parts of a list:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```

### Useful patterns:

- `[:3]` → start to index 3
    
- `[2:]` → index 2 to end
    
- `[-3:]` → last 3 items
    

---

## Copying Lists

Correct way (independent copy):

```python
my_foods = ['pizza', 'falafel']
friend_foods = my_foods[:]
```

Wrong way (linked lists):

```python
friend_foods = my_foods
```

---

## Tuples

Tuples are immutable (cannot be changed).

```python
dimensions = (200, 50)
```

### Looping through tuple:

```python
for value in dimensions:
    print(value)
```

### Reassigning tuple:

```python
dimensions = (400, 100)
```

---

## PEP 8 Style Guide

### Key rules:

- 4 spaces per indentation
    
- max ~80 characters per line
    
- use blank lines to organize code
    
- keep code readable
    

---

# Try It Yourself

## 4-1 Pizzas

- Create a list of pizzas
    
- Use a loop to print each pizza
    
- Print a sentence about each pizza
    
- Add a final message outside the loop
    

---

## 4-2 Animals

- Create a list of animals
    
- Print each animal
    
- Print a fact about each animal
    
- Add a final message about their similarity
    

---

## 4-3 Counting to Twenty

Print numbers from 1 to 20 using a loop.

---

## 4-4 One Million

Create a list from 1 to 1,000,000 and loop through it.

---

## 4-5 Summing a Million

- Use `min()`
    
- Use `max()`
    
- Use `sum()`
    

---

## 4-6 Odd Numbers

Use `range()` step to generate odd numbers.

---

## 4-7 Threes

Generate multiples of 3.

---

## 4-8 Cubes

Create cubes using `value**3`.

---

## 4-9 Cube Comprehension

Do the same using list comprehension.

---

## 4-10 Slices

- First 3 items
    
- Middle 3 items
    
- Last 3 items
    

---

## 4-11 My Pizzas, Your Pizzas

- Copy a list
    
- Modify both lists differently
    
- Show they are independent
    

---

## 4-12 More Loops

Use loops to print multiple lists.

---

## 4-13 Buffet

- Create tuple of foods
    
- Loop through it
    
- Try modifying (should fail)
    
- Reassign tuple
    

---

## Footnotes