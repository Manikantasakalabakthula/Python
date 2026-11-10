"""
Exercise 3 - Sum of Two Numbers

Task:
Write a program that takes two numbers as input from the user, calculates their sum using integer type conversion, and prints the result.

Requirements:

- Prompt the user to enter a first number using the prompt message: `Enter the first number: `
- Prompt the user to enter a second number using the prompt message: `Enter the second number: `
- Convert both user inputs from strings to integers using `int()`.
- Add the two integer values together and store the result in a variable named `sum`.
- Print the value of `sum`.

Example:

Input:
Enter the first number: 15
Enter the second number: 25

Output:
40

"""

first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
sum=first_number+second_number
print(sum)