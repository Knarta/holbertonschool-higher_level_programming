# Python - Data Structures: Lists, Tuples 📚

## Learning Objectives 🎯
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome 🐍
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing and sequence unpacking
- What is the `del` statement and how to use it

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
### 0. Print a list of integers 🔢
- Write a function that prints all integers of a list:
  - Prototype: `def print_list_integer(my_list=[]):`
  - Format: one integer per line. See example
  - You are not allowed to import any module
  - You can assume that the list only contains integers
  - You are not allowed to cast integers into strings
  - You have to use `str.format()` to print integers

#### Example:
```python
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
# Output:
# 1
# 2
# 3
# 4
# 5
```

### 1. Secure access to an element in a list 🔒
- Write a function that retrieves an element from a list:
  - Prototype: `def element_at(my_list, idx):`
  - If idx is negative, the function should return None
  - If idx is out of range (> of number of element in my_list), the function should return None
  - You are not allowed to import any module
  - You are not allowed to use try/except

#### Example:
```python
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
# Output: Element at index 3 is 4
```

### 2. Replace element 🔄
- Write a function that replaces an element of a list at a specific position:
  - Prototype: `def replace_in_list(my_list, idx, element):`
  - If idx is negative, the function should not modify anything, and returns the original list
  - If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
  - You are not allowed to import any module
  - You are not allowed to use try/except

#### Example:
```python
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
# Output: [1, 2, 3, 9, 5]
print(my_list)
# Output: [1, 2, 3, 9, 5]
```

### 3. Print a list of integers... in reverse! 🔄
- Write a function that prints all integers of a list, in reverse order:
  - Prototype: `def print_reversed_list_integer(my_list=[]):`
  - Format: one integer per line. See example
  - You are not allowed to import any module
  - You can assume that the list only contains integers
  - You are not allowed to cast integers into strings
  - You have to use `str.format()` to print integers

#### Example:
```python
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
# Output:
# 5
# 4
# 3
# 2
# 1
```

### 4. Replace in a copy 🔄
- Write a function that replaces an element in a list at a specific position without modifying the original list:
  - Prototype: `def new_in_list(my_list, idx, element):`
  - If idx is negative, the function should return a copy of the original list
  - If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
  - You are not allowed to import any module
  - You are not allowed to use try/except

#### Example:
```python
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
# Output: [1, 2, 3, 9, 5]
print(my_list)
# Output: [1, 2, 3, 4, 5]
```

### 5. Can you C me now? 👀
- Write a function that removes all characters c and C from a string:
  - Prototype: `def no_c(my_string):`
  - The function should return the new string
  - You are not allowed to import any module
  - You are not allowed to use `str.replace()`

#### Example:
```python
#!/usr/bin/python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
# Output: Best Shool
print(no_c("Chicago"))
# Output: hiago
print(no_c("C is fun!"))
# Output:  is fun!
```

### 6. Lists of lists = Matrix 🔲
- Write a function that prints a matrix of integers:
  - Prototype: `def print_matrix_integer(matrix=[[]]):`
  - Format: see example
  - You are not allowed to import any module
  - You can assume that the list only contains integers
  - You are not allowed to cast integers into strings
  - You have to use `str.format()` to print integers

#### Example:
```python
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
# Output:
# 1 2 3
# 4 5 6
# 7 8 9
print("--")
print_matrix_integer()
# Output:
#
```

### 7. Tuples addition ➕
- Write a function that adds 2 tuples:
  - Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
  - Returns a tuple with 2 integers:
    - The first element should be the addition of the first element of each argument
    - The second element should be the addition of the second element of each argument
  - You are not allowed to import any module
  - You can assume that the two tuples will only contain integers
  - If a tuple is smaller than 2, use the value 0 for each missing integer
  - If a tuple is bigger than 2, use only the first 2 integers

#### Example:
```python
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)
# Output: (89, 100)

print(add_tuple(tuple_a, (1, )))
# Output: (2, 89)
print(add_tuple(tuple_a, ()))
# Output: (1, 89)
```

### 8. More returns! 🔄
- Write a function that returns a tuple with the length of a string and its first character:
  - Prototype: `def multiple_returns(sentence):`
  - If the sentence is empty, the first character should be equal to None
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
# Output: Length: 22 - First character: A
```

### 9. Find the max 🔝
- Write a function that finds the biggest integer of a list:
  - Prototype: `def max_integer(my_list=[]):`
  - If the list is empty, return None
  - You can assume that the list only contains integers
  - You are not allowed to import any module
  - You are not allowed to use the builtin `max()`

#### Example:
```python
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
# Output: Max: 90
```

### 10. Only by 2 ✌️
- Write a function that finds all multiples of 2 in a list:
  - Prototype: `def divisible_by_2(my_list=[]):`
  - Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
  - The new list should have the same size as the original list
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
# Output:
# 0 is divisible by 2
# 1 is not divisible by 2
# 2 is divisible by 2
# 3 is not divisible by 2
# 4 is divisible by 2
# 5 is not divisible by 2
# 6 is divisible by 2
```

### 11. Delete at 🗑️
- Write a function that deletes the item at a specific position in a list:
  - Prototype: `def delete_at(my_list=[], idx=0):`
  - If idx is negative or out of range, nothing change (returns the same list)
  - You are not allowed to use `pop()`
  - You are not allowed to import any module

#### Example:
```python
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
# Output: [1, 2, 3, 5]
print(my_list)
# Output: [1, 2, 3, 5]
```

### 12. Switch 🔄
- Complete the source code in order to switch value of a and b:
  - You can find the source code [here](https://github.com/holbertonschool/0x03.py/blob/master/12-switch.py)
  - Your code should be inserted where the comment is (line 4)
  - Your program should be exactly 5 lines long

#### Example:
```python
a = 89
b = 10
# ... your code here ...
print("a={:d} - b={:d}".format(a, b))
# Output: a=10 - b=89
```

## Repo 📂
- GitHub repository: holbertonschool-higher_level_programming
- Directory: python-data_structures