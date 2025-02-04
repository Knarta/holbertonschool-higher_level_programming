# Python - More Classes and Objects 🧩

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
- What is the difference between a class attribute and an instance attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
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
### 0. Simple rectangle 🟦
- Write an empty class Rectangle that defines a rectangle:
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
# Output: <class '0-rectangle.Rectangle'>
print(my_rectangle.__dict__)
# Output: {}
```

### 1. Real definition of a rectangle 🟧
- Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
  - Private instance attribute: width:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
      - width must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
      - if width is less than 0, raise a ValueError exception with the message `width must be >= 0`
  - Private instance attribute: height:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
      - height must be an integer, otherwise raise a TypeError exception with the message `height must be an integer`
      - if height is less than 0, raise a ValueError exception with the message `height must be >= 0`
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)
# Output: {'_Rectangle__width': 2, '_Rectangle__height': 4}

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
# Output: {'_Rectangle__width': 10, '_Rectangle__height': 3}
```

### 2. Area and Perimeter 📏
- Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
  - Private instance attribute: width:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
      - width must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
      - if width is less than 0, raise a ValueError exception with the message `width must be >= 0`
  - Private instance attribute: height:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
      - height must be an integer, otherwise raise a TypeError exception with the message `height must be an integer`
      - if height is less than 0, raise a ValueError exception with the message `height must be >= 0`
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if width or height is equal to 0, perimeter is equal to 0
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
# Output: Area: 8 - Perimeter: 12

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
# Output: Area: 30 - Perimeter: 26
```

### 3. String representation 🖋️
- Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
  - Private instance attribute: width:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
      - width must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
      - if width is less than 0, raise a ValueError exception with the message `width must be >= 0`
  - Private instance attribute: height:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
      - height must be an integer, otherwise raise a TypeError exception with the message `height must be an integer`
      - if height is less than 0, raise a ValueError exception with the message `height must be >= 0`
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if width or height is equal to 0, perimeter has to be equal to 0
  - `print()` and `str()` should print the rectangle with the character `#`:
    - if width or height is equal to 0, return an empty string
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
# Output: Area: 8 - Perimeter: 12

print(str(my_rectangle))
# Output:
# ##
# ##
# ##
# ##

print(repr(my_rectangle))
# Output: <3-rectangle.Rectangle object at 0x7f92a75a2eb8>

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
# Output:
# ##########
# ##########
# ##########

print(repr(my_rectangle))
# Output: <3-rectangle.Rectangle object at 0x7f92a75a2eb8>
```

### 4. Eval is magic 🧙‍♂️
- Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
  - Private instance attribute: width:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
      - width must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
      - if width is less than 0, raise a ValueError exception with the message `width must be >= 0`
  - Private instance attribute: height:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
      - height must be an integer, otherwise raise a TypeError exception with the message `height must be an integer`
      - if height is less than 0, raise a ValueError exception with the message `height must be >= 0`
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if width or height is equal to 0, perimeter has to be equal to 0
  - `print()` and `str()` should print the rectangle with the character `#`:
    - if width or height is equal to 0, return an empty string
  - `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
# Output:
# ##
# ##
# ##
# ##

print("--")
print(my_rectangle)
# Output:
# ##
# ##
# ##
# ##

print("--")
print(repr(my_rectangle))
# Output: Rectangle(2, 4)

print("--")
print(hex(id(my_rectangle)))
# Output: 0x7f09ebf7cc88

print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
# Output:
# ##
# ##
# ##
# ##

print("--")
print(new_rectangle)
# Output:
# ##
# ##
# ##
# ##

print("--")
print(repr(new_rectangle))
# Output: Rectangle(2, 4)

print("--")
print(hex(id(new_rectangle)))
# Output: 0x7f09ebf7ccc0

print("--")

print(new_rectangle is my_rectangle)
# Output: False
print(type(new_rectangle) is type(my_rectangle))
# Output: True
```

### 5. Detect instance deletion 🗑️
- Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
  - Private instance attribute: width:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
      - width must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
      - if width is less than 0, raise a ValueError exception with the message `width must be >= 0`
  - Private instance attribute: height:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
      - height must be an integer, otherwise raise a TypeError exception with the message `height must be an integer`
      - if height is less than 0, raise a ValueError exception with the message `height must be >= 0`
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if width or height is equal to 0, perimeter has to be equal to 0
  - `print()` and `str()` should print the rectangle with the character `#`:
    - if width or height is equal to 0, return an empty string
  - `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  - Print the message `Bye rectangle...` when an instance of Rectangle is deleted
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
# Output: Area: 8 - Perimeter: 12

del my_rectangle
# Output: Bye rectangle...

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
# Output: [NameError] name 'my_rectangle' is not defined
```

### 6. How many instances 🔢
- Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
  - Private instance attribute: width:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
      - width must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
      - if width is less than 0, raise a ValueError exception with the message `width must be >= 0`
  - Private instance attribute: height:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
      - height must be an integer, otherwise raise a TypeError exception with the message `height must be an integer`
      - if height is less than 0, raise a ValueError exception with the message `height must be >= 0`
  - Public class attribute `number_of_instances`:
    - Initialized to 0
    - Incremented during each new instance instantiation
    - Decremented during each instance deletion
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if width or height is equal to 0, perimeter has to be equal to 0
  - `print()` and `str()` should print the rectangle with the character `#`:
    - if width or height is equal to 0, return an empty string
  - `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  - Print the message `Bye rectangle...` when an instance of Rectangle is deleted
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
# Output: 2 instances of Rectangle

del my_rectangle_1
# Output: Bye rectangle...
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
# Output: 1 instances of Rectangle

del my_rectangle_2
# Output: Bye rectangle...
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
# Output: 0 instances of Rectangle
```

### 7. Change representation 🔄
- Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)
  - Private instance attribute: width:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
      - width must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
      - if width is less than 0, raise a ValueError exception with the message `width must be >= 0`
  - Private instance attribute: height:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
      - height must be an integer, otherwise raise a TypeError exception with the message `height must be an integer`
      - if height is less than 0, raise a ValueError exception with the message `height must be >= 0`
  - Public class attribute `number_of_instances`:
    - Initialized to 0
    - Incremented during each new instance instantiation
    - Decremented during each instance deletion
  - Public class attribute `print_symbol`:
    - Initialized to `#`
    - Used as symbol for string representation
    - Can be any type
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if width or height is equal to 0, perimeter has to be equal to 0
  - `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`:
    - if width or height is equal to 0, return an empty string
  - `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  - Print the message `Bye rectangle...` when an instance of Rectangle is deleted
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
# Output:
# ########
# ########
# ########
# ########

print("--")
my_rectangle_
