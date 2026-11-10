"""
Exercise 10 — Arithmetic Calculator

Write a program that:
- Takes two numbers as input.
- Prints:
  - Sum
  - Difference
  - Product
  - Division
  - Floor division
  - Remainder
  - First number raised to the power of the second number

Example:
Enter first number: 10
Enter second number: 3

Sum: 13
Difference: 7
Product: 30
Division: 3.3333333333333335
Floor Division: 3
Remainder: 1
Power: 1000
"""

first_number=int(input("Enter first number: "))
second_number=int(input("Enter second number: "))
print("Sum: ",first_number+second_number)
print("Difference: ",first_number-second_number)
print("Product: ",first_number*second_number)
print("Division: ",first_number/second_number)
print("Floor Division: ",first_number//second_number)
print("Remainder: ",first_number%second_number)
print("Power: ",first_number**second_number)