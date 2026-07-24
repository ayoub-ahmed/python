# Chapter 05 — If Statements

## 📖 Overview

Programming is all about making decisions.

The `if` statement allows your program to execute different code depending on whether a condition is **True** or **False**.

This chapter introduces:

- Conditional Tests
- Boolean Expressions
- Comparison Operators
- `if`
- `if-else`
- `if-elif-else`
- Multiple `if` Statements
- Using `if` with Lists
- Best Practices (PEP 8)

---

# 🧠 Conditional Tests

A **Conditional Test** is an expression that evaluates to either:

- `True`
- `False`

Python uses this result to decide whether code should execute.

Example:

```python
car = "bmw"

car == "bmw"
```

Output

```python
True
```

---

# ⚖️ Equality Operator (`==`)

Checks whether two values are equal.

```python
car = "bmw"

if car == "bmw":
    print("Correct!")
```

Remember:

```python
=
```

Assignment

```python
==
```

Comparison

---

# ❌ Inequality Operator (`!=`)

Checks whether two values are **not equal**.

```python
requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")
```

---

# 🔤 Case Sensitivity

Python compares strings exactly.

```python
"Audi" == "audi"
```

Result

```python
False
```

To ignore capitalization:

```python
car.lower() == "audi"
```

The original variable remains unchanged.

---

# 🔢 Numerical Comparisons

Python supports normal mathematical comparisons.

| Operator | Meaning |
|----------|---------|
| `==` | Equal |
| `!=` | Not Equal |
| `>` | Greater Than |
| `<` | Less Than |
| `>=` | Greater or Equal |
| `<=` | Less or Equal |

Example:

```python
age = 19

age >= 18
```

Output

```python
True
```

---

# 🔗 Multiple Conditions

Sometimes one condition is not enough.

Python provides:

- `and`
- `or`

---

## ✅ and

Both conditions must be True.

```python
age_0 = 22
age_1 = 22

age_0 >= 21 and age_1 >= 21
```

Result

```python
True
```

---

## ✅ or

Only one condition needs to be True.

```python
age_0 = 22
age_1 = 18

age_0 >= 21 or age_1 >= 21
```

Result

```python
True
```

---

# 📋 Membership Operators

## in

Checks whether a value exists inside a list.

```python
requested_toppings = [
    "mushrooms",
    "onions",
    "pineapple"
]

"mushrooms" in requested_toppings
```

Output

```python
True
```

---

## 🚫 not in

Checks whether a value does **not** exist.

```python
banned_users = [
    "andrew",
    "carolina",
    "david"
]

user = "marie"

if user not in banned_users:
    print("You can post.")
```

---

# 🔘 Boolean Values

Boolean values are simply:

```python
True
False
```

Example:

```python
game_active = True

can_edit = False
```

Used to represent the state of a program.

---

# 🌱 Simple if Statement

Runs code only if the condition is True.

Syntax:

```python
if condition:
    do_something()
```

Example:

```python
age = 19

if age >= 18:
    print("You can vote.")
```

---

# 🔀 if-else Statement

Choose between two actions.

```python
age = 17

if age >= 18:
    print("You can vote.")
else:
    print("Too young.")
```

Only one block executes.

---

# 🌳 if-elif-else Chain

Used when there are multiple possibilities.

Example:

```python
age = 12

if age < 4:
    price = 0

elif age < 18:
    price = 25

else:
    price = 40
```

Python checks conditions from top to bottom.

As soon as one condition becomes True:

- It executes that block.
- Skips the remaining conditions.

---

# ➕ Multiple elif Blocks

You may add as many `elif` blocks as necessary.

```python
if age < 4:
    ...

elif age < 18:
    ...

elif age < 65:
    ...

else:
    ...
```

Useful when handling several categories.

---

# 🚫 Omitting else

Sometimes using another `elif` is safer.

Instead of:

```python
else:
```

Use:

```python
elif age >= 65:
```

This avoids accidentally handling unexpected data.

---

# ⚠️ Independent if Statements

Use separate `if` statements when **multiple conditions may all be True**.

Example:

```python
requested_toppings = [
    "mushrooms",
    "extra cheese"
]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")

if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")

if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
```

Output

```text
Adding mushrooms.
Adding extra cheese.
```

---

# ❗ if vs if-elif

## Use `if-elif-else`

When only **one** choice should happen.

Example:

Choosing one ticket price.

---

## Use multiple `if`

When multiple actions may occur.

Example:

Adding several pizza toppings.

---

# 🍕 Using if with Lists

Lists become much more powerful with `if`.

---

## Handling Special Items

```python
for topping in requested_toppings:

    if topping == "green peppers":
        print("Sorry, out of stock.")

    else:
        print(f"Adding {topping}")
```

Perfect for handling exceptions.

---

# 📭 Checking for an Empty List

Instead of checking the length:

```python
if requested_toppings:
```

Python interprets:

- Non-empty list → `True`
- Empty list → `False`

Example:

```python
requested_toppings = []

if requested_toppings:
    print("Making pizza.")
else:
    print("Plain pizza?")
```

---

# 📚 Using Multiple Lists

Compare one list against another.

Example:

```python
available_toppings = [
    "mushrooms",
    "olives",
    "pepperoni",
    "extra cheese"
]

requested_toppings = [
    "mushrooms",
    "french fries",
    "extra cheese"
]
```

```python
for topping in requested_toppings:

    if topping in available_toppings:
        print(f"Adding {topping}")

    else:
        print(f"Sorry, we don't have {topping}")
```

Very common in real-world programs.

---

# 🎨 Styling if Statements (PEP 8)

Use spaces around comparison operators.

✅ Good

```python
if age >= 18:
```

❌ Bad

```python
if age>=18:
```

Proper spacing improves readability.

---

# 📝 Commands & Keywords Learned

| Keyword / Operator | Purpose |
|--------------------|---------|
| `if` | Execute code conditionally |
| `else` | Alternative block |
| `elif` | Additional condition |
| `==` | Equal |
| `!=` | Not Equal |
| `>` | Greater Than |
| `<` | Less Than |
| `>=` | Greater or Equal |
| `<=` | Less or Equal |
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `in` | Membership test |
| `not in` | Negative membership test |
| `True` | Boolean True |
| `False` | Boolean False |

---

# 💡 Real-World Applications

- 👤 User authentication
- 🛒 Online shopping carts
- 🍕 Food ordering systems
- 🎮 Game logic
- 🌐 Website permissions
- 📊 Data filtering
- 📝 Form validation
- 🚦 Decision making in programs

---

# 🎯 Key Takeaways

- Every `if` statement depends on a **conditional test**.
- Conditional tests always evaluate to **True** or **False**.
- `=` assigns values, while `==` compares values.
- `!=` checks inequality.
- String comparisons are **case-sensitive** unless you use `.lower()`.
- Use comparison operators (`>`, `<`, `>=`, `<=`) for numbers.
- Use `and` when **all** conditions must be true.
- Use `or` when **at least one** condition is enough.
- Use `in` and `not in` to test list membership.
- Use `if` for one conditional action.
- Use `if-else` when there are exactly two outcomes.
- Use `if-elif-else` when only one of several choices should execute.
- Use multiple independent `if` statements when several actions may all need to run.
- Empty lists evaluate to `False`; non-empty lists evaluate to `True`.
- Combining lists with `if` statements is a common pattern in real-world Python programs.
- Follow **PEP 8** by adding spaces around comparison operators to keep code clean and readable.




# Try It Yourself

## 5-1 Conditional Tests

- Write 10 conditional tests
- Predict each result
- Include 5 `True` and 5 `False`

---

## 5-2 More Conditional Tests

- Equality and inequality
- `lower()`
- Numerical comparisons
- `and`
- `or`
- `in`
- `not in`

---

## 5-3 Alien Colors #1

- Create `alien_color`
- Print 5 points if green
- Create a version where nothing is printed

---

## 5-4 Alien Colors #2

- Use `if-else`
- Green → 5 points
- Otherwise → 10 points

---

## 5-5 Alien Colors #3

- Use `if-elif-else`
- Green → 5 points
- Yellow → 10 points
- Red → 15 points

---

## 5-6 Stages of Life

Determine the life stage using an `if-elif-else` chain.

---

## 5-7 Favorite Fruit

- Create `favorite_fruits`
- Use independent `if` statements
- Print a message for each favorite fruit

---

## 5-8 Hello Admin

- Loop through usernames
- Special greeting for `admin`
- Normal greeting for other users

---

## 5-9 No Users

- Check if the users list is empty
- Print a message if it is

---

## 5-10 Checking Usernames

- Create `current_users`
- Create `new_users`
- Check username availability
- Ignore letter case

---

## 5-11 Ordinal Numbers

- Loop through numbers 1–9
- Use `if-elif-else`
- Print the correct ordinal number

---

## 5-12 Styling if Statements

Review your code and follow **PEP 8**.

---

## 5-13 Your Ideas

Write down programming ideas for future projects.