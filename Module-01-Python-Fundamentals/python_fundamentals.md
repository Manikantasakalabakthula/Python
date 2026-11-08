# Module 1 — Python Fundamentals

## Topic 1: Introduction to Python

### Python

- Python is a **high-level, interpreted, general-purpose programming language**.
- It was created by **Guido van Rossum** and created in **1989**.
- It was released to the public in **1991** with version **0.9.0**.
- It emphasizes **code readability and simplicity** using indentation to define code blocks.

### Why Python?

- It is easy to learn and read.
- It is free to use and open-source.
- Millions of developers and libraries are available.

### Features of Python

- Python has simple syntax.
- It runs anywhere with the same code.
- It manages memory and variables automatically.

### Applications of Python

- Data Science & Analytics
- Artificial Intelligence & Machine Learning
- Software and Web Development
- Automation & Testing

### Limitations of Python

- Executes code line-by-line, so the speed is slow.
- Rarely used for building mobile apps.
- Consumes more RAM due to automatic data tracking.

### Python Interpreter

- A built-in software program that runs Python code.
- It executes the code line-by-line.

---

# Topic 2: Python Basic Syntax

## Python Syntax

```python
a = 10
print(a)
```

### Indentation

- Python uses **4 empty spaces** at the start of a line.
- If wrong indentation occurs in the code, it shows an error called **IndentationError**.

### Comments

- Use the `#` symbol to write single-line comments.
- Triple quotes can be used to write multi-line comments/docstrings.

#### Example

```python
# Single-line comment
```

```python
"""
This is a multi-line comment
"""
```

### Case Sensitivity

- Small and capital letters are treated as completely different things.

For example:

```python
name = "Manikanta"
Name = "Adithya"
```

Here, `name` and `Name` are different identifiers.

---

# Topic 3: Output — `print()`

## `print()` Function

- It displays text, numbers, and multiple data.
- Put your data inside parentheses and separate multiple values with commas.

### Syntax

```python
print(value)
```

### Example

```python
print("Age", 20)
```

### Output

```text
Age 20
```

### Common Mistake

- Forgetting to write commas when printing multiple values.

---

## `sep` Parameter

- `sep` is a character placed between multiple printed items.

### Syntax

```python
print(value1, value2, sep="character")
```

### Example

```python
print("Apple", "Banana", sep=",")
```

### Output

```text
Apple,Banana
```

### Common Mistake

- Putting `sep` at the start instead of using it as a keyword argument.

---

## `end` Parameter

- The `end` parameter specifies what is printed at the very end of the line instead of moving to a new line.

### Syntax

```python
print(value, end="character")
```

### Example

```python
print("Hello World", end="!")
```

### Output

```text
Hello World!
```

---

## Escape Sequence — `\n` and `\t`

- Escape sequences are special code combinations used inside text quotes.
- They can be used to add a **new line** or **wide tab spaces**.

### Syntax

```python
"\n"
"\t"
```

### Example

```python
print("Line1\nLine2")
print("Item:\tApple")
```

### Output

```text
Line1
Line2
Item:   Apple
```

---

# Topic 4: Input — `input()`

## `input()` Function

- `input()` is a way to ask the user for input and save the text inside a variable.
- `input()` always stores the user's input as a **string**, even if the user enters a number.
- For type conversion with `input()`, we can use `int(input())` or `float(input())` to perform mathematical operations.

### Syntax

```python
variable_name = input("prompt")
variable = int(input())
variable = float(input())
```

### Example

```python
name = input("Enter your name: ")
print(name)

age = int(input("Enter your age: "))
print(age)
```

### Example Output

```text
Enter your name: Manikanta
Enter your age: 20
20
```

---

# Topic 5: Variables & Identifiers

## Variables

- Variables are named containers used to store values.
- Stored values can include data types such as numbers, strings, or lists.
- The values can be changed using the same variable name, which overwrites the previous value.
- We can assign multiple values to multiple variables in a single line.

### Syntax

```python
variable_name = value
```

```python
x, y = value1, value2
```

```python
a = b = c = value
```

### Examples

```python
name = "Manikanta"
print(name)

name = "Adithya"
print(name)

x, y = 5, 10

a = b = c = 10

print(x, y, a, b, c)
```

### Output

```text
Manikanta
Adithya
5 10 10 10 10
```

---

## Variable Naming Rules & Identifiers

- Variable names should be meaningful.
- A variable name must start with either a **letter** or an **underscore**.
- Variable names can contain **alphanumeric characters** and underscores only.
- Special symbols and spaces are not allowed.
- Variable names are **case-sensitive**.
- Variable names should not be reserved words/keywords.
- Variable names cannot start with numbers.

### Examples

```text
name
age
_age
id
id1
roll_no
RollNo
```

---

## Multi-Word Variable Names

### 1. Camel Case

- Each word except the first word starts with a capital letter.

Example:

```python
myVariableName
```

### 2. Pascal Case

- Each word starts with a capital letter.

Example:

```python
MyVariableName
```

### 3. Snake Case

- Each word is separated by an underscore.

Example:

```python
my_variable_name
```

---

# Topic 6: Python Keywords

## Python Keywords

- Python keywords are **pre-defined, reserved words** that have a fixed and special meaning to the interpreter.
- You cannot use them as regular variable names.
- They form the structural building blocks of Python code.

### Checking Python Keywords

The `keyword` module can be used to check whether a word is a Python keyword.

### Example

```python
import keyword

print("Is 'if' a keyword?:", keyword.iskeyword("if"))
print("Is 'apple' a keyword?:", keyword.iskeyword("apple"))
```

### Output

```text
Is 'if' a keyword?: True
Is 'apple' a keyword?: False
```

---

# Topic 7: Python Data Types

## Data Types

- Data types tell the type of a value/data.
- Data types are actually **classes in Python**, and variables are objects of their classes.
- In Python, the user does not need to specify the type of a variable while executing the code because Python determines it automatically.
- Python has multiple data types.

### Common Python Data Types

1. **Numeric types**
   - `int`
   - `float`
   - `complex`

2. **String**
   - `str`

3. **Sequence types**
   - `list`
   - `tuple`
   - `range`

4. **Mapping type**
   - `dict`

5. **Boolean type**
   - `bool`

6. **Set type**
   - `set`

---

## Integer — `int`

- `int` contains whole numbers, either positive or negative.
- There is no fixed limit to how long an integer value can be, subject to available memory.

### Example

```python
a = 123
print(a)

a = 123456789101213
print(a)
```

---

## Integer Prefixes

With specific prefixes, numbers can be represented in different bases.

### Binary — Base 2

Prefix:

```text
0b
```

Example:

```python
0b11
```

Output:

```text
3
```

### Octal — Base 8

Prefix:

```text
0o
```

Example:

```python
0o11
```

Output:

```text
9
```

### Hexadecimal — Base 16

Prefix:

```text
0x
```

Example:

```python
0x11
```

Output:

```text
17
```

### Examples

```python
print(0b11)    # 3
print(0o11)    # 9
print(0x11)    # 17
```

> Note: A prefix determines the number's base. For example, `0b123` is invalid because binary digits can only be `0` and `1`.

### Checking the Type

Use `type()` to check the type of a variable.

```python
a = 10
print(type(a))
```

---

## Float — `float`

- Float values represent decimal numbers.

### Examples

```python
b = 5.523
print(b)

b = 18.2546892034
print(b)
```

---

## String — `str`

- Strings are sequences of characters.
- They are enclosed by **double quotes** or **single quotes**.

### Examples

```python
name = "Manikanta"
name = 'Manikanta'
```

### String Indexing

- Indexing is used to access a character at a particular index of a string.
- String indexing starts from `0`.

### Example

```python
print("Manikanta")
print("Manikanta"[3])
```

Output:

```text
Manikanta
i
```

---

## Boolean — `bool`

- Boolean has two possible values:
  - `True`
  - `False`
- It is useful for decision-making.
- `True` and `False` must start with capital letters.

### Example

```python
a = True
b = False

print(a)
print(b)
```

---

# Topic 8: Type Conversion / Casting

## Type Conversion / Type Casting

- Type conversion means changing a value from one data type to another.
- It is useful to avoid errors when working with different data types, such as numbers and text.
- Python supports both **implicit** and **explicit** type conversion.

### Two Types

1. **Implicit Type Conversion**
2. **Explicit Type Conversion**

---

## Implicit Type Conversion

- Python automatically converts one data type to another compatible data type without the programmer explicitly calling a conversion function.
- This generally happens when converting a value to a type that can safely represent it, such as `int` to `float`.

### Example

```python
a = 10
b = 10.5

result = a + b
print(result)
```

### Output

```text
20.5
```

Here, Python automatically converts the integer `10` to a float during the operation.

---

## Explicit Type Conversion

- The programmer manually converts one data type into another using built-in functions.

Common conversion functions:

```python
int()
float()
str()
bool()
```

### Example 1 — String to Integer

```python
a = "10"

print(10 + int(a))
```

### Output

```text
20
```

### Example 2 — String to Float

```python
b = "10.5"

print(10 + float(b))
```

### Output

```text
20.5
```

### Example 3 — String to Integer

```python
c = "123"

new_c = int(c)

print(10 + new_c)
```

### Output

```text
133
```

### Invalid Conversion

If a string does not contain a valid numeric value, converting it to `int` or `float` can cause a `ValueError`.

For example:

```python
d = "Manikanta"

print(int(d))
```

This produces a `ValueError` because `"Manikanta"` cannot be converted into an integer.

---

# Quick Revision

| Topic | Important Points |
|---|---|
| Python | High-level, interpreted, general-purpose language |
| Syntax | Python uses indentation |
| Comments | `#` for single-line comments |
| Output | `print()` |
| Input | `input()` |
| Variables | Store values |
| Identifiers | Names given to variables, functions, etc. |
| Keywords | Reserved words with special meaning |
| Integer | `int` |
| Decimal | `float` |
| Text | `str` |
| Boolean | `bool` |
| Type Conversion | Changing one data type into another |
| Implicit Conversion | Done automatically by Python |
| Explicit Conversion | Done manually using functions such as `int()` and `float()` |