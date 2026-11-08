# Module - 02 : Operators

Operators - Operators are used to perform some operations on values.
- Operators are special symbols like +, -, /, *, etc.
- Operand is the value on which the operators are applied.
- Eg:- 2 + 3 = 5, 2 * 3 = 6
  (Here, +, * are operators & 2 & 3 are operands)

- Types of operators :-
  1) Arithmetic operators
  2) Comparision / relational operators
  3) Logical operators
  4) Assignment operators
  5) Bitwise operators
  6) Special
     - Identity operators
     - Membership operators

### 1) Arithmetic operators:-
These are used to perform mathematical operations like, add, subtract, multiply, divide, floor division, modulus & power

- Eg:-
```python
a = 10
b = 5

print(a + b)  # => 15
print(a - b)  # => 5
print(a * b)  # => 50
print(a / b)  # => 2
```

---


### 2) Comparison operator:
- In this operator, the values are compares and return either true or false according to the condition.
- ==, <, >, <=, >=, != are the operators in this comparison operator.

- Eg:
```python
a = 10
b = 5

print(a == b)  # => False
print(a < b)   # => False
print(a > b)   # => True
print(a <= b)  # => False
print(a >= b)  # => True
print(a != b)  # => True
```

---


### 3) Assignment operator:
- In this operator, used to assign value to variables.
- Also used Arithmetic operations to assign the variables.
- We can assign more than one variables in 1 line.
- =, +=, -=, *=, /=, %=, //=, **= are the operations in this Assignment operator.

- Eg:-
```python
a = 10
b = 5

print(a += b, a -= b, a *= b, a /= b, a %= b, a //= b, a **= b)  # => (15, 5, 50, 2, 0, 2, 100000)
```

---


### 4) Logical operators :-
- Basically used to combine conditional statements.
- AND, OR, NOT are logical operators

**Truth Table**

| X | Y | AND | OR | NOT X | NOT Y |
|---|---|-----|----|-------|-------|
| True | True | True | True | False | False |
| True | False | False | True | False | True |
| False | True | False | True | True | False |
| False | False | False | False | True | True |

- AND will return True if both are true
- OR will return True if one is true
- NOT reverse the result.

```python
a = 5
b = 4

# - Eg:
print(a < 5 and b == 4)  # => False
print(a <= 5 and b == 4) # => True
print(a < 5 or b == 4)   # => True
```

---


### 5) Membership operators:
- Membership operators checks for membership in a sequence such a strings, list & tuples, set, dictionary
- There are 2 types: in, not in

- in : returns True if specified element is present in the sequence otherwise return False;
- not in : returns True if specified element is not present in the sequence, otherwise return False.

- Eg:
```python
str = "manikanta"

print('k' in str)      # => True
print('a' in str)      # => True
print('v' in str)      # => False
print('v' not in str)  # => True
print('n' not in str)  # => False

l1 = [1, 2, 3, 4, 5]
print(10 in l1)        # => False
print(-5 not in l1)    # => True
```

---


### 6) Identity operator:
- Compare the objects to check if both the objects are actually same objects and share same memory location.
- Python is purely object based language. So everything in python is an object & every object is stored at a memory location. So each object is having its own unique id.
- To find Id of an object
  Syntax :- id(object_name)
- So it will return memory address of the object (which have been passed as an argument).
- Memory manages in python reuses the objects instead of creating another object for the same data & with same data type.
- There are two types:-
  1) is
  2) is not

#### - is operator:
- returns True, if both variable are same object (or) both operands have same unique Id otherwise it returns False.

- Eg:-
```python
# 1)
a = 10
b = 10
print(a is b)  # => True
```
```text
   a        b
    \      /
     [ 10 ]
     ID-1000
```

```python
# 2)
a = 10
b = 10.2
print(a is b)  # => False
```
```text
     a          b
     |          |
   [ 10 ]    [ 10.2 ]
   ID-1000   ID-2000
```

```python
# 3)
a = 10
b = '10'
print(a is b)  # => False
```
```text
     a          b
     |          |
   [ 10 ]    [ '10' ]
   ID-1000   ID-2000
```

```python
# 4)
a = 10
print(id(a))  # => 140737399313816

b = 10
print(id(b))  # => 140737399313816

c = 9
print(id(c))  # => 140737399313784
```

#### - is not :
- returns True if memory location of two objects are not same
- returns False if memory location of two objects are same

- Note: Identity operator is not Equality operator
  - Equality operator (==) checks for equality of value are equal or not
  - But Identity operators checks the memory location of objects.

- Eg:-
```python
a = 10
b = 10
c = 9
d = "10"

print(a is not b)  # => False
print(a is not c)  # => True
print(a is not d)  # => True
```
```text
   a        b
    \      /
     [ 10 ]
     ID-1

     a          c
     |          |
   [ 10 ]     [ 9 ]
   ID-1       ID-2

     a          d
     |          |
   [ 10 ]    [ "10" ]
   ID-1       ID-3
```

---


### 7) Bitwise operators:-
- Bitwise operators works on bits.
- used to compare binary numbers
- There are 6 types of bitwise operators.
- They are:
  - & (Bitwise AND)
  - | (OR)
  - ^ (XOR)
  - ~ (NOT / compliment)
  - << (left shift)
  - >> (right shift)

- We use 8 4 2 1 to calculate binary numbers.
- For example,
```text
a = 10
b = 8

            8 4 2 1
binary of a = 1 0 1 0
binary of b = 1 0 0 0
```

#### 1) & (Bitwise AND):
- For &, 1 & 1 is true, 0 & 0 is false, 1 & 0 is false.
- Eg:
```python
a = 10
b = 8

print(a & b)  # => 8
```
```text
 10 = 1 0 1 0
  8 = 1 0 0 0
-------------
10 & 8 = 1 0 0 0 => 8
```

#### 2) | (OR) :
- For |, 1 | 1 is true, 0 | 0 is false, 1 | 0 is true
- Eg:-
```python
a = 10
b = 8

print(a | b)  # => 10
```
```text
 10 = 1 0 1 0
  8 = 1 0 0 0
-------------
10 | 8 = 1 0 1 0 => 10
```

#### 3) ^ (XOR) :
- For ^, 1 ^ 1 is 0, 0 ^ 0 is 0 & 1 ^ 0 is 1
- If both bits are different sets 1 otherwise 0.
- Eg:-
```python
a = 10
b = 8

print(a ^ b)  # => 2
```
```text
 10 = 1 0 1 0
  8 = 1 0 0 0
-------------
10 ^ 8 = 0 0 1 0 => 2
```

#### 4) ~ (NOT (compliment)) :
- For ~, ~0 = 1
- ~1 = 0
- ~ will do reverse of the bit
- Eg:-
```python
a = 10
b = 8

print(~a)  # => -11
print(~b)  # => -9
```
```text
 10 = 1010
~10 = 0101 => 5
  2's = 1's + 1

  1's of ~10 = 1010
  2's of ~10 = 1010
                 +1
               ----
               1011 => -11

  8 = 1000
 ~8 = 0111 => 7
  2's = 1's + 1

  1's of ~8 = 1000 (POV)
  2's of ~8 = 1000
                +1
              ----
              1001 => -9
```

#### 5) << (left shift) :
- It shifts the bits of first operand with respect to second operand.
- Shifts left by pushing zeros in from the right & let the left most bits fall off.
- In left shift we gain bits.

- Eg:
```python
a = 10
print(a << 4)  # => 160
```
```text
10 => 1 0 1 0

  128 64 32 16 8 4 2 1
  ---------------------
  1   0  1  0  0 0 0 0  => 128 + 32 = 160
```

```python
b = 8
print(b << 6)  # => 512
```
```text
8 => 1000

  512 256 128 64 32 16 8 4 2 1
  -----------------------------
  1   0   0   0   0  0  0 0 0 0  => 512
```

#### 6) >> (right shift) :
- It shifts right by pushing zeros in from the left & let the right most bits fall off.
- In right shift we lose bits.

- Eg :-
```python
a = 10
print(a >> 4)  # => 0
```
```text
10 => 1010
      xxxx
      0000 => 0
```

```python
b = 8
print(b >> 6)  # => 0
```
```text
8 => 1000
     xxxx
     0000 => 0
```

### Exercise -
```python
print(26 & 23)  # => 18
```
```text
26 => 0 1 1 0 1 0
23 => 0 1 0 1 1 1
-----------------
      0 1 0 0 1 0 => 18
```

```python
print(17 | 24)  # => 25
```
```text
17 => 0 1 0 0 0 1
24 => 0 1 1 0 0 0
-----------------
      0 1 1 0 0 1 => 25
```

```python
print(17 ^ 24)  # => 9
```
```text
17 => 0 1 0 0 0 1
24 => 0 1 1 0 0 0
-----------------
      0 0 1 0 0 1 => 9
```

```python
print(~45)  # => -46
```
```text
      45 => 1 0 1 1 0 1
     ~45 => 0 1 0 0 1 0
     1's => 1 0 1 1 0 1
2's = (1's + 1) => 1 0 1 1 1 0 => 46
(~45 =>) -46
```

```python
print(68 << 2)  # => 272
```
```text
68 => 0 1 0 0 0 1 0 0
      0 1 0 0 0 1 0 0 0 0 => 272
```

```python
print(56 >> 3)  # => 7
```
```text
56 => 0 0 1 1 1 0 0 0
      0 0 0 0 0 1 1 1 => 7
```

---


### Operator precedence:
- In some calculations, multiple operators are used then we have to follow precedence rule.
- The calculation will follows PEMDAS rule:
  1) Parenthesis ()
  2) Exponent **
  3) Multiplication & division * or /
  4) Addition & subtraction + or -

- If in the calculation, we have all the above operators, then we are confuse to which operator solve first.
- Here is the solutions which prefer first (* or /) and (+ or -) comes associativity into picture.
- Associativity for these operator are Left -> Right
- For Exponent has Right -> Left associativity

- Eg:-
```python
5 + 2 * 3 - 1 + 10 / 5  # => 12.0
# ->
5 + 2 * (3 - 1) + 10 / 5  # => 11.0
```