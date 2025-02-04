# Python - Test-driven development 🧪


## Learning Objectives 🎯
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome 🐍
- What is TDD and why is it important
- What are docstrings and how to use them
- How to write a test case
- What is the difference between a unit test and an integration test
- What are the common testing frameworks in Python
- How to write a test suite
- How to run tests using unittest
- How to find bugs using tests
- How to use the assert statement in tests

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
### 0. Integers addition ➕
- Write a function that adds 2 integers:
  - Prototype: `def add_integer(a, b=98):`
  - a and b must be integers or floats, otherwise raise a TypeError exception with the message `a must be an integer` or `b must be an integer`
  - a and b must be first casted to integers if they are float
  - Returns an integer: the addition of a and b
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))  # Output: 3
print(add_integer(100, -2))  # Output: 98
print(add_integer(2))  # Output: 100
print(add_integer(100.3, -2))  # Output: 98
```

### 1. Divide a matrix ➗
- Write a function that divides all elements of a matrix:
  - Prototype: `def matrix_divided(matrix, div):`
  - matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message `matrix must be a matrix (list of lists) of integers/floats`
  - Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message `Each row of the matrix must have the same size`
  - div must be a number (integer or float), otherwise raise a TypeError exception with the message `div must be a number`
  - div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message `division by zero`
  - All elements of the matrix should be divided by div, rounded to 2 decimal places
  - Returns a new matrix
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
# Output: [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
```

### 2. Say my name 🗣️
- Write a function that prints `My name is <first name> <last name>`:
  - Prototype: `def say_my_name(first_name, last_name=""):`
  - first_name and last_name must be strings otherwise, raise a TypeError exception with the message `first_name must be a string` or `last_name must be a string`
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
# Output: My name is John Smith
say_my_name("Walter", "White")
# Output: My name is Walter White
say_my_name("Bob")
# Output: My name is Bob
```

### 3. Print square ⬛
- Write a function that prints a square with the character #:
  - Prototype: `def print_square(size):`
  - size is the size length of the square
  - size must be an integer, otherwise raise a TypeError exception with the message `size must be an integer`
  - if size is less than 0, raise a ValueError exception with the message `size must be >= 0`
  - if size is a float and is less than 0, raise a TypeError exception with the message `size must be an integer`
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
# Output:
# ####
# ####
# ####
# ####
```

### 4. Text indentation 📄
- Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
  - Prototype: `def text_indentation(text):`
  - text must be a string, otherwise raise a TypeError exception with the message `text must be a string`
  - There should be no space at the beginning or at the end of each printed line
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? Non autem hoc: igitur ne illud quidem.")
# Output:
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#
# Quonam modo?
#
# Utrum igitur tibi litteram videor an totas paginas commovere?
#
# Non autem hoc:
#
# igitur ne illud quidem.
```

### 5. Max integer - Unittest 🧪
- Write unittests for the function `def max_integer(list=[]):`
  - Your test file should be inside a folder `tests`
  - You have to use the `unittest` module
  - Your test file should be python files (extension: .py)
  - Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
  - All tests you make must be passable by the function below
  - We strongly encourage you to work together on test cases, so that you don’t miss any edge case

#### Example:
```python
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
# Output: 4
print(max_integer([1, 3, 4, 2]))
# Output: 4
```

## Repo 📂
- GitHub repository: holbertonschool-higher_level_programming
- Directory: python-test_driven_development
