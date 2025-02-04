# Python - Inheritance 📚

## Resources 📖
Read or watch:
- [Object Oriented Programming](https://example.com)
- [Object-Oriented Programming](https://example.com)
- [Class and Instance Attributes](https://example.com)
- [classmethods and staticmethods](https://example.com)
- [Properties vs. Getters and Setters](https://example.com)
- [str vs repr](https://example.com)

## Learning Objectives 🎯
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome 🐍
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- What are the special __str__ and __repr__ methods and how to use them
- What is the difference between __str__ and __repr__
- What is a class attribute
- What is the difference between an object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to objects and classes
- What is and what does contain __dict__ of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the getattr function

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
### 0. Lookup
- Write a function that returns the list of available attributes and methods of an object:
  - Prototype: `def lookup(obj):`
  - Returns a list object
  - You are not allowed to import any module

### 1. My list
- Write a class `MyList` that inherits from `list`:
  - Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
  - You can assume that all the elements of the list will be of type int
  - You are not allowed to import any module

### 2. Exact same object
- Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.
  - Prototype: `def is_same_class(obj, a_class):`
  - You are not allowed to import any module

### 3. Same class or inherit from
- Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.
  - Prototype: `def is_kind_of_class(obj, a_class):`
  - You are not allowed to import any module

### 4. Only sub class of
- Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
  - Prototype: `def inherits_from(obj, a_class):`
  - You are not allowed to import any module

### 5. Geometry module
- Write an empty class `BaseGeometry`.
  - You are not allowed to import any module

### 6. Improve Geometry
- Write a class `BaseGeometry` (based on `5-base_geometry.py`).
  - Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`
  - You are not allowed to import any module

### 7. Integer validator
- Write a class `BaseGeometry` (based on `6-base_geometry.py`).
  - Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`
  - Public instance method: `def integer_validator(self, name, value):` that validates value:
    - you can assume name is always a string
    - if value is not an integer: raise a TypeError exception, with the message `<name> must be an integer`
    - if value is less or equal to 0: raise a ValueError exception with the message `<name> must be greater than 0`
  - You are not allowed to import any module

### 8. Rectangle
- Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).
  - Instantiation with width and height: `def __init__(self, width, height):`
  - width and height must be private. No getter or setter
  - width and height must be positive integers, validated by `integer_validator`

### 9. Full rectangle
- Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)
  - Instantiation with width and height: `def __init__(self, width, height):`
  - width and height must be private. No getter or setter
  - width and height must be positive integers validated by `integer_validator`
  - the `area()` method must be implemented
  - `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

### 10. Square #1
- Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):
  - Instantiation with size: `def __init__(self, size):`
  - size must be private. No getter or setter
  - size must be a positive integer, validated by `integer_validator`
  - the `area()` method must be implemented

### 11. Square #2
- Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).
  - Instantiation with size: `def __init__(self, size):`
  - size must be private. No getter or setter
  - size must be a positive integer, validated by `integer_validator`
  - the `area()` method must be implemented
  - `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

## Repo 📂
- GitHub repository: holbertonschool-higher_level_programming
- Directory: python-inheritance
