"""
Exercise 12 — Membership & Identity

Write a program with:
name = "Python Programming"


Check and print whether:
- "Python" is present in name
- "Java" is present in name
- "Java" is not present in name

Then create:
a = [1, 2, 3]b = ac = [1, 2, 3]


Print the results of:
a == b
a is b
a == c
a is c

Important: Don't just guess the last four outputs. Think about value equality vs object identity.
"""

name = "Python Programming"
print("Python" in name)
print("Java" in name)
print("Java" not in name)
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)
print(a is b)
print(a == c)
print(a is c)