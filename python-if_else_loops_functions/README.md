# Python - If/Else, Loops, Functions 🔄

## Learning Objectives 🎯
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome 🐍
- Why indentation is so important in Python
- How to use the `if`, `if ... else` statements
- How to use comments
- How to affect values to variables
- How to use the `while` and `for` loops
- How is Python’s `for` different from C‘s?
- How to use the `break` and `continues` statements
- How to use `else` clauses on loops
- What does the `pass` statement do, and when to use it
- How to use `range`
- What is a function and how do you use functions
- What does return a function that does not use any `return` statement
- Scope of variables
- What’s a traceback
- What are the arithmetic operators and how to use them

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
### 0. Positive anything is better than negative nothing ➕
- This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative:
  - You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative.py)
  - The variable `number` will store a different value every time you will run this program
  - You don’t have to understand what `import`, `random.randint` do. Please do not touch this code
  - The output of the program should be:
    - The number, followed by
    - if the number is greater than 0: `is positive`
    - if the number is 0: `is zero`
    - if the number is less than 0: `is negative`
    - followed by a new line

#### Example:
```python
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# ...existing code...
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
# Output:
# -4 is negative
# 0 is zero
# 10 is positive
```

### 1. The last digit 🔢
- This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`:
  - You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit.py)
  - The variable `number` will store a different value every time you will run this program
  - You don’t have to understand what `import`, `random.randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000, 10000)`
  - The output of the program should be:
    - The string `Last digit of`, followed by
    - the number, followed by
    - the string `is`, followed by the last digit of `number`, followed by
    - if the last digit is greater than 5: the string `and is greater than 5`
    - if the last digit is 0: the string `and is 0`
    - if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
    - followed by a new line

#### Example:
```python
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# ...existing code...
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
print("Last digit of {} is {} and is ".format(number, last_digit), end="")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
# Output:
# Last digit of 4205 is 5 and is less than 6 and not 0
# Last digit of -626 is -6 and is less than 6 and not 0
# Last digit of 5247 is 7 and is greater than 5
```

### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game 🔤
- Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line:
  - Use only one `print` function with string format
  - Use only one loop in your code
  - You are not allowed to store characters in a variable
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
for i in range(97, 123):
    print("{}".format(chr(i)), end="")
# Output: abcdefghijklmnopqrstuvwxyz
```

### 3. When I was having that alphabet soup, I never thought that it would pay off 🍲
- Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line:
  - Print all the letters except `q` and `e`
  - You can only use one `print` function with string format
  - You can only use one loop in your code
  - You are not allowed to store characters in a variable
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end="")
# Output: abcdfghijklmnoprstuvwxyz
```

### 4. Hexadecimal printing 🔢
- Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example):
  - You can only use one `print` function with string format
  - You can only use one loop in your code
  - You are not allowed to store numbers or strings in a variable
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
for i in range(99):
    print("{} = {}".format(i, hex(i)))
# Output:
# 0 = 0x0
# 1 = 0x1
# 2 = 0x2
# ...
# 98 = 0x62
```

### 5. 00...99 🔢
- Write a program that prints numbers from 0 to 99:
  - Numbers must be separated by `,`, followed by a space
  - Numbers should be printed in ascending order, with two digits
  - The last number should be followed by a new line
  - You can only use no more than 2 `print` functions with string format
  - You can only use one loop in your code
  - You are not allowed to store numbers or strings in a variable
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
for i in range(100):
    if i < 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
# Output:
# 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
```

### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need 🧠
- Write a program that prints all possible different combinations of two digits:
  - Numbers must be separated by `,`, followed by a space
  - The two digits must be different
  - `01` and `10` are considered the same combination of the two digits `0` and `1`
  - Print only the smallest combination of two digits
  - Numbers should be printed in ascending order, with two digits
  - The last number should be followed by a new line
  - You can only use no more than 3 `print` functions with string format
  - You can only use no more than 2 loops in your code
  - You are not allowed to store numbers or strings in a variable
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end="")
# Output:
# 01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
```

### 7. islower 🔡
- Write a function that checks for lowercase character:
  - Prototype: `def islower(c):`
  - Returns `True` if `c` is lowercase
  - Returns `False` otherwise
  - You are not allowed to import any module
  - You are not allowed to use `str.upper()` and `str.isupper()`
  - Tips: `ord()`
  - You don’t need to understand `__import__`

#### Example:
```python
#!/usr/bin/python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
# Output: a is lower
print("H is {}".format("lower" if islower("H") else "upper"))
# Output: H is upper
print("A is {}".format("lower" if islower("A") else "upper"))
# Output: A is upper
print("3 is {}".format("lower" if islower("3") else "upper"))
# Output: 3 is upper
print("g is {}".format("lower" if islower("g") else "upper"))
# Output: g is lower
```

### 8. To uppercase 🔠
- Write a function that prints a string in uppercase followed by a new line:
  - Prototype: `def uppercase(str):`
  - You can only use no more than 2 `print` functions with string format
  - You can only use one loop in your code
  - You are not allowed to import any module
  - You are not allowed to use `str.upper()` and `str.isupper()`
  - Tips: `ord()`
  - You don’t need to understand `__import__`

#### Example:
```python
#!/usr/bin/python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
# Output: BEST
uppercase("Best School 98 Battery street")
# Output: BEST SCHOOL 98 BATTERY STREET
```

### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important 🎨
- Write a function that prints the last digit of a number:
  - Prototype: `def print_last_digit(number):`
  - Returns the value of the last digit
  - You are not allowed to import any module
  - You don’t need to understand `__import__`

#### Example:
```python
#!/usr/bin/python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
# Output: 8
print_last_digit(0)
# Output: 0
r = print_last_digit(-1024)
print(r)
# Output: 4
```

### 10. a + b ➕
- Write a function that adds two integers and returns the result:
  - Prototype: `def add(a, b):`
  - Returns the value of `a + b`
  - You are not allowed to import any module
  - You don’t need to understand `__import__`

#### Example:
```python
#!/usr/bin/python3
add = __import__('10-add').add

print(add(1, 2))
# Output: 3
print(add(98, 0))
# Output: 98
print(add(100, -2))
# Output: 98
```

### 11. a ^ b 🔢
- Write a function that computes `a` to the power of `b` and return the value:
  - Prototype: `def pow(a, b):`
  - Returns the value of `a ^ b`
  - You are not allowed to import any module
  - You don’t need to understand `__import__`

#### Example:
```python
#!/usr/bin/python3
pow = __import__('11-pow').pow

print(pow(2, 2))
# Output: 4
print(pow(98, 2))
# Output: 9604
print(pow(98, 0))
# Output: 1
print(pow(100, -2))
# Output: 0.0001
print(pow(-4, 5))
# Output: -1024
```

### 12. Fizz Buzz 🍾
- Write a function that prints the numbers from 1 to 100 separated by a space:
  - For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
  - For numbers which are multiples of both three and five print `FizzBuzz`.
  - Prototype: `def fizzbuzz():`
  - Each element should be followed by a space
  - You are not allowed to import any module
  - You don’t need to understand `__import__`

#### Example:
```python
#!/usr/bin/python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")
# Output:
# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz
```

## Repo 📂
- GitHub repository: holbertonschool-higher_level_programming
- Directory: python-if_else_loops_functions
