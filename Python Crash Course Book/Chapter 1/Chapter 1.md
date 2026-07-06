
# Getting Started — Python Setup & First Program

## 1. Overview
In this chapter, you set up your Python programming environment and run your first program: **hello_world.py**.  
You also install a text editor and learn how Python programs are executed.

---

## 2. Setting Up Your Programming Environment
Python works slightly differently across operating systems, so setup may vary.  
Before writing code, you must:

- Install **Python (3.6 or later)**
- Install a **text editor (Sublime Text recommended)**

Text editors help by:
- Highlighting Python syntax
- Making code structure easier to read
- Allowing quick program execution

---

## 3. Python Versions
Python is continuously updated.

- Latest version mentioned: **Python 3.7**
- Minimum required for this book: **Python 3.6+**
- You should use **Python 3**, NOT Python 2

> Python 2 is outdated and may still exist for legacy system programs.

---

## 4. Running Python Snippets
Python can be run interactively in a terminal using the interpreter:

```bash
>>> print("Hello Python interpreter!")
Hello Python interpreter!
````

Key points:

- `>>>` means you are inside the Python shell
    
- Used for quick testing and learning
    
- Exit using:
    
    - `exit()`
        
    - or `Ctrl + D`
        

---

## 5. Text Editor: Sublime Text

Sublime Text is a lightweight editor used to:

- Write Python files (`.py`)
    
- Run code directly inside the editor
    
- Show output in an embedded terminal
    

Benefits:

- Beginner-friendly
    
- Used by professionals
    
- Free to use (license encouraged for support)
    

---

## 6. Python Across Operating Systems

### 🪟 Windows

- Python may NOT be installed by default
    
- Install from: [https://python.org/](https://python.org/)
    
- Important step: ✔ Add Python to PATH
    

Run Python:

```bash
python
```

---

### 🍎 macOS

- Often comes with Python 2 (outdated)
    
- Install Python 3 manually
    

Check version:

```bash
python3 --version
```

Run Python:

```bash
python3
```

---

### 🐧 Linux

- Python is usually pre-installed
    

Check version:

```bash
python3
```

---

## 7. Installing Sublime Text

Download from:  
[https://sublimetext.com/](https://sublimetext.com/)

Then install depending on OS:

- Windows: Run installer
    
- macOS: Drag to Applications
    
- Linux: Install via Software Center
    

---

## 8. Running Your First Program

### Create File

Create a folder:

```
python_work/
```

Inside it, create:

```
hello_world.py
```

### Code:

```python
print("Hello Python world!")
```

---

## 9. Running the Program

### Inside Sublime Text

- Press:
    
    - `Ctrl + B` (Windows/Linux)
        
    - `Cmd + B` (macOS)
        

Output:

```text
Hello Python world!
```

---

## 10. Running from Terminal

### Windows

```bash
cd Desktop\python_work
dir
python hello_world.py
```

### macOS / Linux

```bash
cd Desktop/python_work/
ls
python3 hello_world.py
```

---


## 11. 🧪 Try It Yourself (IMPORTANT SECTION)

### 1-1. python.org Exploration

Visit [https://python.org/](https://python.org/) and explore:

- Documentation
- Tutorials
- News and updates

---

### 1-2. Hello World Typos

Open `hello_world.py` and:

- Introduce a typo
- Run the program again

Try to observe:

- What errors appear?
- Which typos break the program?
- Which do NOT?

Understand why Python behaves this way.

---

### 1-3. Infinite Skills

Imagine:

- If you had unlimited programming skills, what would you build?

Write down 3 ideas like:

- Apps
- Games
- Tools
- Automation scripts

This helps you form real project goals early.

## 12. Common Errors & Troubleshooting


If something goes wrong:

- Check syntax carefully (Python is strict)
    
- Look at error traceback messages
    
- Common mistakes:
    
    - Missing quotes `" "`
        
    - Missing parentheses `()`
        
    - Wrong capitalization (`Print` vs `print`)
        
- Restart and try again if needed
    

---

## 13. Key Concepts Learned

- Installing Python
    
- Checking Python version
    
- Using terminal & Python shell
    
- Writing a `.py` file
    
- Running programs in:
    
    - Editor (Sublime Text)
        
    - Terminal
        
- Basic troubleshooting
    

---

## 14. Summary

You learned how to:

- Install Python and a text editor
    
- Confirm Python works on your system
    
- Run code in interactive mode
    
- Write and execute your first program: **hello_world.py**
    

Next chapter will cover:

> Variables and data types in Python