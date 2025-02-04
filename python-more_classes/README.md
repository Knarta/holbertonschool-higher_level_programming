# Python - More Classes and Objects 📚

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
### 0. Simple rectangle
- Write an empty class Rectangle that defines a rectangle:
  - You are not allowed to import any module

### 1. Real definition of a rectangle
- Write a class Rectangle that defines a rectangle by:
  - Private instance attribute: width
  - Private instance attribute: height
  - Instantiation with optional width and height

### 2. Area and Perimeter
- Write a class Rectangle that defines a rectangle by:
  - Public instance method: def area(self): that returns the rectangle area
  - Public instance method: def perimeter(self): that returns the rectangle perimeter

### 3. String representation
- Write a class Rectangle that defines a rectangle by:
  - print() and str() should print the rectangle with the character #

### 4. Eval is magic
- Write a class Rectangle that defines a rectangle by:
  - repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()

### 5. Detect instance deletion
- Write a class Rectangle that defines a rectangle by:
  - Print the message Bye rectangle... when an instance of Rectangle is deleted

### 6. How many instances
- Write a class Rectangle that defines a rectangle by:
  - Public class attribute number_of_instances

### 7. Change representation
- Write a class Rectangle that defines a rectangle by:
  - Public class attribute print_symbol

### 8. Compare rectangles
- Write a class Rectangle that defines a rectangle by:
  - Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area

### 9. A square is a rectangle
- Write a class Rectangle that defines a rectangle by:
  - Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size

## Repo 📂
- GitHub repository: holbertonschool-higher_level_programming
- Directory: python-more_classes
