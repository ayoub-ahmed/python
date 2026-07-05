# Introducing Lists

## 1. Overview
Lists allow you to store **multiple values in a single variable**.

They are:
- Ordered collections
- Flexible (can store any type of data)
- One of Python’s most powerful beginner tools

---

## 2. What Is a List?

A list is created using square brackets `[]`:

```python id="l1x9a2"
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
````

Output:

```text
['trek', 'cannondale', 'redline', 'specialized']
```

---

## 3. Accessing List Elements

You access items using **index positions**:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```

Output:

```text
trek
```

### Important Rule

Python starts counting at **0**. [1]

---

## 4. Negative Indexing

```python
print(bicycles[-1])
```

- `-1` → last item
    
- `-2` → second last item
    

---

## 5. Using List Values

```python
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
```

---

## 6. Try It Yourself (IMPORTANT)

### 3-1 Names

- Store friends in a list
    
- Print each name individually
    

### 3-2 Greetings

- Print personalized messages
    

### 3-3 Your Own List

- Create a list of favorite transportation
    
- Print sentences about each item
    

---

## 7. Modifying Lists

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
```

---

## 8. Adding Elements

### append()

```python
motorcycles.append('ducati')
```

### insert()

```python
motorcycles.insert(0, 'ducati')
```

---

## 9. Removing Elements

### del (delete by index)

```python
del motorcycles[0]
```

---

### pop() (remove + keep value)

```python
last = motorcycles.pop()
```

---

### remove() (delete by value)

```python
motorcycles.remove('ducati')
```

---

## 10. Sorting Lists

### Permanent sort

```python
cars.sort()
```

### Reverse sort

```python
cars.sort(reverse=True)
```

---

## 11. Temporary Sorting

```python
print(sorted(cars))
```

---

## 12. Reversing Lists

```python
cars.reverse()
```

---

## 13. Length of a List

```python
len(cars)
```

---

## 14. Common Error — Index Error

```python
print(motorcycles[3])
```

Error:

- `IndexError: list index out of range`
    

[2]

---

## 15. Try It Yourself (IMPORTANT)

### 3-4 Guest List

- Invite 3+ people using a list
    

### 3-5 Changing Guests

- Replace a guest
    
- Update invitations
    

### 3-6 More Guests

- Use insert + append
    

### 3-7 Shrinking List

- Remove guests using pop()
    
- End with 2 guests only
    

---

## 16. Key Concepts Summary

You learned:

- What lists are
    
- Indexing (0-based system)
    
- Adding, changing, removing elements
    
- Sorting and reversing lists
    
- List length
    
- Common index errors
    

---

## References

[1] Python uses zero-based indexing (first element is index 0)  
[2] IndexError happens when you access a non-existing position