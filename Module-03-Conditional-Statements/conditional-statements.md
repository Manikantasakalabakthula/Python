# Module 03 : Control Flow & Conditionals

### round() function:-
- It is inbuilt function in Python
- used to round off numbers upto the specified number of decimal points.
- Syntax: `round(number, ndigits)`
- number is must to specify, it is the number to be rounded off.
- ndigits are optional, it is the number upto which the given number is rounded. by default ndigits are considered as zero.

#### What round() will return?
It will return the
- case 1 : nearest integer to the given number if n digits is not given.
- case 2 : number rounded off to n digits digits if n digits is given.

- Eg:
```python
print(round(10))           # => 10
print(round(10.5))         # => 10
print(round(3.3333, 2))    # => 3.33
print(round(3.3366, 2))    # => 3.34
print(round(7.66657, 0))   # => 8.0
```

- In first case of return, the type would be int.
- In case 2, type would be float
- If number is equally nearby before or after number then it returns nearest even number

- Eg:
```python
print(round(7.5))  # => 8
print(round(3.5))  # => 4
print(round(2.5))  # => 2
```

- In round() function, number can not be string, it should be integer or floating number.

#### Note :-
1. If ndigits is a positive value, then round off has no effect on the integer value (number)
   - Eg:-
   ```python
   print(round(674, 2))  # => 674
   ```

2. If ndigits is zero value, then round off has no effect on the integer value (number)
   - Eg:-
   ```python
   print(round(674, 0))  # => 674
   ```

3. If n digits is negative value, then round off has effects the integer value (number). Here, we use $10^{-(\text{negative } n \text{ digit})}$
   - Eg:-
   ```python
   print(round(674, -1))  # => 670
   print(round(674, -2))  # => 700
   ```

4. But if the absolute value of negative decimal points is greater than the number of digits in the original number then the input number becomes zero.
   - Eg:-
   ```python
   print(round(670, -4))  # => 0
   ```

5. In this also, if number is nearly equal to before and after number then it returns nearest even number.

---

### f-strings :-
- f-strings provide a faster, more readable, more concise & less error prone way of formatting strings in python.
- f-strings use `f` as prefix & `{}` brackets to evaluate value.
- In `{}` brackets there are expressions that will be replaced with their values.

- Eg:-
```python
name = "Manikanta"
age = 23
height = 5.7

print(f"my name is {name}, I am {age} years old, my height is {height} ft")
```

---


### Control flow :-
- Control flow is the order of execution in which the statements of a program.
- By default, python executes statements from top to bottom, one after another.
- Control flow statements allow us to change this normal flow based on conditions.

- Eg:-
```python
print("start")  # => start   | TOP
print("Hello")  # => Hello   | to
print("End")    # => End     V Bottom
```

### Sequential vs conditional execution:-
- In sequential execution, statements are executed one after another in the order which they are written.
- Eg:-
```python
a = 10
b = 20
c = a + b
print(c)  # => 30
```
```text
Flow:
a = 10
  ↓
b = 20
  ↓
c = a + b
  ↓
print(a + b)
```

- In conditional execution, a particular block of code executes only when a specific condition is satisfied.
- Python uses `if`, `elif` & `else` for conditional execution.
- They also called conditional statements.
- Eg:-
```python
a = 10
if a == 10:
    pass

a = 10
if a < 10:
    print('a: ', a)
```

### Indentation in Python:-
- Indentation means spaces at the beginning of a line of code.
- Python uses indentation to identify a block of code.
- use 4 spaces for one level of indentation.
- Eg:-
  - Correct:
  ```python
  if 10 > 5:
      print("10 is greater")
  ```
  - Incorrect:
  ```python
  if 10 > 5:
  print("10 is greater")
  ```

### Code blocks:-
- A group of statements that belongs together and executed as a unit.
- In Python, indentation is key for code block.
- If we not provide indentation for specific code blocks, it will shows indentation error.

- Eg:-
```python
if 10 > 5:
    print("condition is true")   # one block of code

print("outside the if block")    # other block of code
```

### Nested code blocks:-
- A block can contain another block.
- Eg:-
```python
if 10 > 5:
    print("outer block")         # outside block
    if 20 > 10:
        print("Inner block")     # inside block
```

---


### if statement :-
- A simplest decision-making statement
- If given condition is true then a block of statement would be executed otherwise not.

- Eg:-
```python
if 5 > 10:
    print("5 is less than 10")

print("out of if block")
```
- O/P:- `out of if block`

---


### if-else statement:-
- A decision making statement
- The if-else statement is used when you want to execute one block of code if a condition is true, another block of code if a condition is false.

- Eg:
```python
age = 16

if age >= 18:
    print("adult")       # condition: False
else:
    print("minor")       # It executes
```
- O/P - `minor`

---


### if-elif-else statement:-
- If we need to make a choice between more than two choices then we use `elif` statement.

- Syntax:
```python
if condition1:
    # Code block 1
elif condition2:
    # Code block 2
elif condition3:
    # Code block 3
    # :
else:
    # Code block else
```

- Eg:-
```python
a = 10
b = 15
c = 20

if a > b:
    print(a)
elif b > c:
    print(b)
elif a > c:
    print(c)
else:
    print(f"a: {a}, b: {b} and c: {c}")
```

---


### Nested if and if-else statement:-

#### Nested if :
- if inside if that means if statement inside if statement.

- Syntax:
```python
if condition1:
    if condition2:
        # code block 1
```

- Eg:
```python
a = 52

if a % 2 == 0:
    if a > 10:
        print("Even and a > 10")
```

#### Nested if-else :
- In this case an entire if...else construct is written within either the body of if statement or the body of else statement.

- Syntax:
```python
if condition1:
    if condition2:
        # code block 1
    else:
        # code block 2
```

- Eg:
```python
a = 30

if a % 2 == 0:
    if a > 10:
        print("even and a > 10")
    else:
        print("even and a < 10")
```

---


### Ternary operator:
- A short way of writing a simple if-else.

- Syntax: `value_if_true if condition else value_if_false`

- Eg:-
```python
age = 20

result = "Adult" if age >= 18 else "Minor"
print(result)
```

---


### match-case :
- match-case is used to compare a value against different possible patterns and execute the matching block.

- Syntax:
```python
match value:
    case pattern1:
        # code
    case pattern2:
        # code
```
- It is useful when you have multiple possible values to check.

- Eg:
```python
day = 3

match day:
    case 1:
        print("M")
    case 2:
        print("T")
    case 3:
        print("W")
```
- O/P: `W`

- The `_` pattern works like a default case. It runs when none of previous cases match.

---


### Combining conditions:-
- Conditions can be combined using comparison, logical and membership operators.

- Eg:
```python
age = 20
percentage = 75
name = "python"
marks = [75, 80, 90]

if (age > 18 and age < 25 and age >= 18 and age <= 25 and age == 20 and age != 15 and percentage >= 60 and not(percentage < 50) and name in "python programming" and "Java" not in name and 75 in marks):
    print("Eligible")
```