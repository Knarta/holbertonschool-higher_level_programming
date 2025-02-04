# Python - Import & Modules 📦

## Learning Objectives 🎯
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome 🐍
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## Requirements ✅
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Tasks 📋
### 0. Import a simple function from a simple file ➕
- Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`:
  - You have to use `print` function with string format to display integers
  - You have to assign:
    - the value 1 to a variable called `a`
    - the value 2 to a variable called `b`
    - and use those two variables as arguments when calling the functions `add` and `print`
  - `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`
  - Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
  - You can only use the word `add_0` once in your code
  - You are not allowed to use `*` for importing or `__import__`
  - Your code should not be executed when imported - by using `__import__`, like the example below

#### Example:
```python
#!/usr/bin/python3
from add_0 import add

a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))
# Output: 1 + 2 = 3
```

### 1. My first toolbox! 🧰
- Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result:
  - Do not use the function `print` (with string format to display integers) more than 4 times
  - You have to define:
    - the value 10 to a variable `a`
    - the value 5 to a variable `b`
    - and use those two variables only, as arguments when calling functions (including `print`)
  - `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`
  - Your program should call each of the imported functions. See example below for format
  - The word `calculator_1` should be used only once in your file
  - You are not allowed to use `*` for importing or `__import__`
  - Your code should not be executed when imported

#### Example:
```python
#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

print("{} + {} = {}".format(a, b, add(a, b)))
# Output: 10 + 5 = 15
print("{} - {} = {}".format(a, b, sub(a, b)))
# Output: 10 - 5 = 5
print("{} * {} = {}".format(a, b, mul(a, b)))
# Output: 10 * 5 = 50
print("{} / {} = {}".format(a, b, div(a, b)))
# Output: 10 / 5 = 2
```

### 2. How to make a script dynamic! 📝
- Write a program that prints the number of and the list of its arguments:
  - The output should be:
    - Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
    - `:` (or `.` if no arguments were passed) followed by
    - a new line, followed by (if at least one argument),
    - one line per argument:
      - the position of the argument (starting at 1) followed by `:`, followed by the argument value and a new line
  - Your code should not be executed when imported
  - The number of elements of `argv` can be retrieved by using: `len(argv)`
  - You do not have to fully understand lists yet, but imagine that `argv` can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

#### Example:
```python
#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))
# Output:
# ./2-args.py
# 0 arguments.
# ./2-args.py Hello
# 1 argument:
# 1: Hello
# ./2-args.py Hello Welcome To The Best School
# 6 arguments:
# 1: Hello
# 2: Welcome
# 3: To
# 4: The
# 5: Best
# 6: School
```

### 3. Infinite addition ➕
- Write a program that prints the result of the addition of all arguments:
  - The output should be the result of the addition of all arguments, followed by a new line
  - You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers)
  - Your code should not be executed when imported

#### Example:
```python
#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    result = 0
    for i in range(1, argc + 1):
        result += int(argv[i])

    print(result)
# Output:
# ./3-infinite_add.py
# 0
# ./3-infinite_add.py 79 10
# 89
# ./3-infinite_add.py 79 10 -40 -300 89
# -162
```

### 4. Who are you? 🕵️‍♂️
- Write a program that prints all the names defined by the compiled module `hidden_4.pyc` (please download it locally in your sandbox using `curl`):
  - This task must be done on the sandbox only
  - File `4-hidden_discovery.py` must be located on the folder `/tmp/`
  - You should print one name per line, in alpha order
  - You should print only names that do not start with `__`
  - Your code should not be executed when imported

#### Example:
```python
#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
# Output:
# my_secret_santa
# print_hidden
# print_school
```

### 5. Everything can be imported 📦
- Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value:
  - You are not allowed to use `*` for importing or `__import__`
  - Your code should not be executed when imported

#### Example:
```python
#!/usr/bin/python3
from variable_load_5 import a

print(a)
# Output: 98
```

## Repo 📂
- GitHub repository: holbertonschool-higher_level_programming
- Directory: python-import_modules
