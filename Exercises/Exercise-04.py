"""
Exercise 4 - Sum of Digits of a Two-Digit Number

Task:
Write a program that takes a two-digit number as input from the user, extracts the individual digits using string indexing, converts them into integers, and calculates and prints their sum.

Requirements:

- Prompt the user to enter a two-digit number using the message: `Enter a two digit number: `
- Treat the input as a string to access each digit by its index (`0` for the first digit and `1` for the second digit).
- Convert each extracted digit into an integer.
- Calculate the sum of the two digits and store it in a variable named `sum`.
- Print the final calculated sum.

Example:

Input:
Enter a two digit number: 47

Output:
11
"""

num=input("Enter a two digit number: ")
first_num=int(num[0])
second_num=int(num[1])
sum=first_num+second_num
print(sum)