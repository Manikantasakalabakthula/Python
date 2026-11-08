# Module - 1 (Python Fundamentals)

## Introduction to python

### Python:-
- Python is a high-level, interpreted, general-purpose programming language.
- It is created by Guido van Rossum and created in 1989.
- It is released to the public on 1991 with the version of 0.9.0.
- It emphasizes code readability and simplicity using indentation to define code blocks.

### Why python:-
- It's easy to learn and read.
- It's free to use and open-source.
- Millions of developers and libraries available.

### Features of python:-
- python have simple syntax.
- It runs anywhere with same code.
- It manages memory and variables automatically.

### Application of python:-
- Data Science & Analytics
- Artificial Intelligence & Machine Learning
- Software and Web development.
- Automation & Testing

### Limitation of python:-
- Executes code line-by-line, so the speed is slow.
- Rarely used for building Mobile APPS.
- Consumes more RAM due to automatic data tracking.

### Python Interpreter:-
- A built-in Software program the runs python code.
- It executes the code line-by-line.

---

## python Basic syntax

### Python syntax:-
```python
a = 10
print(a)
```

### Indentation:-
- python uses 4 empty spaces at the start of a line.
- If wrong Indentation occurs in the code that shows error called "Indentation error."

### Comments:-
- use a `#` symbol to write single-line comments.
- use a `""" """` symbols to write multi-line comments.

- Eg:-
```python
# single-line comment

"""
This is Multi-line comment
"""
```

### Case sensitivity:-
- small and capital letters are treated as completely different things.

---

## output - print()

### Print() function:-
- It display text, numbers and multiple data.
- Put your data in round braces and separate multiple values with commas.

- Syntax:
```python
print("Age", 20)
print(Value)
```

- example:
```python
print("Age", 20)
# Output - Age 20
```

### sep Parameter:-
- A character placed between multiple printed items.

- Syntax:
```python
print(value1, value2, sep="character")
```

- eg:-
```python
print("Apple", "Banana", sep=",")
# output: Apple, Banana
```

### end Parameter:-
- the character prints at the very end of the line instead of jumping to new line.

- syntax:
```python
print(value, end="character")
```

- eg:
```python
print("Hello World", end="!")
# output - Hello World!
```

### Escape sequence :- (\n and \t)
- Special code combination used inside text quotes to add new line or wide tab spaces.

- syntax:
```python
"text\ntext"  # or
"text\ttext"
```

- eg:
```python
print("Line 1\nLine 2")
print("Item:\tApple")
```

- output:
```text
Line 1
Line 2
Item:    Apple
```

---

## Input - input()

### Input() function:
- A way to ask the input for user and save the text inside a variable.
- input() always stores user input as a string if it is a number also.
- For type conversion with input(): we can use int(input()) or float(input()) to perform math operations.

- syntax:
```python
variable_name = input("Prompt")
variable = int(input())  # or
variable2 = float(input())
```

- Eg:
```python
name = input("Enter your name: ")
print(name)

age = int(input("Enter your age: "))
print(age)
```

- output:
```text
Enter your name: Manikanta
Enter your age: 
```

---

## Variables & Identifiers

### Variables:-
- Variables are named containers to store the values.
- stored values can be include data types such as numbers, strings, or lists.
- The values are changeable to the same variable name and overwrites the previous value.
- we can assign multiple values to multiple variables in single line.

- syntax:
```python
variable_name = value
x, y = value, value
a = b = c = value
```

- eg:
```python
name = "Manikanta"
print(name)

name = "Adithya"
print(name)

x, y = 5, 10

a = b = c = 10
print(x, y, a, b, c)
```

- output:
```text
Manikanta
Adithya
5, 10, 10, 10, 10
```

### Variable Naming Rules & Identifiers:-
- Variable should be meaningful name
- Must be starts with either letter or underscore
- Variable name can contain alpha-numerical characters and underscore only.
- no other characters like special symbols and spaces are not allowed.
- variable names are case-sensitive
- variable names should not be reserved words.
- can not start with numbers.

- Eg:-
```text
name, age, _age, id, id_1, roll_no, Roll_no
```

### Multi-Word variable names:-
- camel case:- each word except the first letter starts with capital letter
  - eg:- `myVariableName`
- Pascal case:- each word starts with a capital letter.
  - eg:- `MyVariableName`
- Snake case:- each word is separated by underscore
  - eg:- `my_variable_name`

---

## Python keywords

### Python keywords:-
- Python keywords are pre-defined, reserved words that have a fixed, special meaning to the interpreter.
- You can not use them as regular variable names, and they form the structural building blocks of python code.

- syntax:
```python
import keyword
keyword.kwlist
```

- eg:-
```python
import keyword

print("Is 'if' a keyword?: ", keyword.iskeyword("if"))
print("Is 'apple' a keyword?: ", keyword.iskeyword("apple"))
```

- output:
```text
Is 'if' a keyword?: True
Is 'apple' a keyword?: False
```

---

## Python Data types

### Data types:-
- It tells type of value/data.
- Data types are actually classes in python and variables are object of their classes.
- In python user does not need to specify the type of variable while executing the code because python will figure it out.
- Python have multiple data types.
- They are :-
  1) Numeric type - int, float, complex
  2) String
  3) Sequence type - list, tuple, range, dictionary, Boolean, set

#### - int:-
- It contains whole numbers (+ve or -ve)
- There is no limit to how long an integer value.

- Eg:-
```python
a = 123
print(a)

a = 12345678910111213
print(a)
```

- Imp - With any prefix the given numbers would considered as decimal numbers
  - For eg:
    - `0b` or `0B` => Binary (Base 2)
    - `0o` or `0O` => Octal (Base 8)
    - `0x` or `0X` => Hexa (Base 16)

```python
print(0b11)   # => 3
print(0o11)   # => 9
print(0x11)   # => 17

print(0b123)  # => Invalid binary
print(0o123)  # => 83
print(0x123)  # => 291
```

- If you want check the type of the variable use `type()`.

#### Float:-
- They are decimal numbers.

- For eg:
```python
b = 5.523
print(b)  # => 5.523

b = 18.2546892034
print(b)  # => 18.2546892034
```

#### Strings:-
- Strings are sequence of characters.
- They are enclosed by `""` Double or `''` single quotes.
- For eg:- `"Manikanta"` or `'Manikanta'`
- use `string[]` will print the character of the index value of string.

- For eg:-
```python
print("Manikanta")       # => Manikanta
print("Manikanta"[3])    # => i
```

#### Boolean:-
- It have 2 possible value either true or false.
- It is usefull for decision making
- Make sure T & F are capital while using True & False values otherwise you will get errors.

---

## Type conversion/casting

### Type conversion/casting :
- changing a value from one data type to other to avoid errors during actions like mixing numbers and text.
- It can happen automatically by python or manually by built-in functions.
- This lets you to combine strings, integers, numbers and floats without crashing your code.
- There are two types:
  - Implicit: python automatically convert one data type to another without using built-in function
  - Explicit: Manually force a variable to convert one data type to another
- If we convert the text to integer or float it shows value error bcoz text can't convert into integers & float

- Eg:-
```python
# Implicit:
a = "10"
print(10 + int(a))       # => 20

b = "10.5"
print(10 + float(b))     # => 20.5

# Explicit:
c = "123"
new_c = int(c)
print(10 + new_c)        # => 133

# ValueError:
d = "Manikanta"
print(int(d))            # => ValueError
```