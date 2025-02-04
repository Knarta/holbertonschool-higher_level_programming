# Python - Inheritance 🧬

## Learning Objectives 🎯
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome 🐍
- What is inheritance and how to use it
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by inheritance to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

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
### 0. Lookup 🔍
- Write a function that returns the list of available attributes and methods of an object:
  - Prototype: `def lookup(obj):`
  - Returns a list object
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
# Output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
print(lookup(MyClass2))
# Output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
print(lookup(int))
# Output: ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

### 1. My list 📜
- Write a class MyList that inherits from list:
  - Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
  - You can assume that all the elements of the list will be of type int
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
# Output: [1, 4, 2, 3, 5]
my_list.print_sorted()
# Output: [1, 2, 3, 4, 5]
print(my_list)
# Output: [1, 4, 2, 3, 5]
```

### 2. Exact same object 🧩
- Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.
  - Prototype: `def is_same_class(obj, a_class):`
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
# Output: 1 is an instance of the class int
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
```

### 3. Same class or inherit from 🧬
- Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.
  - Prototype: `def is_kind_of_class(obj, a_class):`
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
# Output: 1 comes from int
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
# Output: 1 comes from object
```

### 4. Only sub class of 🧬
- Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
  - Prototype: `def inherits_from(obj, a_class):`
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
# Output: True inherited from class int
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
# Output: True inherited from class object
```

### 5. Geometry module 📐
- Write an empty class BaseGeometry.
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
# Output: <5-base_geometry.BaseGeometry object at 0x7f2050c69208>
print(dir(bg))
# Output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
print(dir(BaseGeometry))
# Output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

### 6. Improve Geometry 📏
- Write a class BaseGeometry (based on 5-base_geometry.py).
  - Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
# Output: [Exception] area() is not implemented
```

### 7. Integer validator 🔢
- Write a class BaseGeometry (based on 6-base_geometry.py).
  - Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`
  - Public instance method: `def integer_validator(self, name, value):` that validates value:
    - you can assume name is always a string
    - if value is not an integer: raise a TypeError exception, with the message `<name> must be an integer`
    - if value is less or equal to 0: raise a ValueError exception with the message `<name> must be greater than 0`
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
# Output: [TypeError] name must be an integer

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
# Output: [ValueError] age must be greater than 0

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
# Output: [ValueError] distance must be greater than 0
```

### 8. Rectangle 🟦
- Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
  - Instantiation with width and height: `def __init__(self, width, height):`
    - width and height must be private. No getter or setter
    - width and height must be positive integers, validated by integer_validator

#### Example:
```python
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
# Output: <8-rectangle.Rectangle object at 0x7f6f488f7eb8>
print(dir(r))
# Output: ['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
# Output: [AttributeError] 'Rectangle' object has no attribute 'width'

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
# Output: [TypeError] height must be an integer
```

### 9. Full rectangle 🟩
- Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
  - Instantiation with width and height: `def __init__(self, width, height):`
    - width and height must be private. No getter or setter
    - width and height must be positive integers validated by integer_validator
  - the `area()` method must be implemented
  - `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

#### Example:
```python
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
# Output: [Rectangle] 3/5
print(r.area())
# Output: 15
```

### 10. Square #1 ⬛
- Write a class Square that inherits from Rectangle (9-rectangle.py):
  - Instantiation with size: `def __init__(self, size):`
    - size must be private. No getter or setter
    - size must be a positive integer, validated by integer_validator
  - the `area()` method must be implemented

#### Example:
```python
#!/usr/bin/python3
Square = __import__('10-square').Square

s = Square(13)

print(s)
# Output: [Rectangle] 13/13
print(s.area())
# Output: 169
```

### 11. Square #2 ⬛
- Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
  - Instantiation with size: `def __init__(self, size):`
    - size must be private. No getter or setter
    - size must be a positive integer, validated by integer_validator
  - the `area()` method must be implemented
  - `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

#### Example:
```python
#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
# Output: [Square] 13/13
print(s.area())
# Output: 169
```

## Repo 📂
- GitHub repository: holbertonschool-higher_level_programming
- Directory: python-inheritance
