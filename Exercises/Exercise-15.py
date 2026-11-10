"""
Exercise 15 — Odd or Even Number Checker

Task:
Write a program that takes an integer from the user and checks whether it is an even or odd number using the modulus operator and an if-else statement.

Requirements:
- Prompt the user to enter a number using: "Enter a number: "
- Convert the input to an integer.
- Check if the number is divisible by 2 using the modulus operator (`%`).
- If divisible by 2 with no remainder, print: `{num} is an Even number`
- Otherwise, print: `{num} is a Odd number`
- Use formatted string literals (f-strings) to display the output.

Example:
Input:
Enter a number: 8

Output:
8 is an Even number

Your task:
Write the Python program yourself. Don't look at the solution first.
For our modules, I'll give you 3–4 coding exercises in this format, increasing from easy → medium → challenging.
And importantly, I won't give the solution along with the question. You write the code first, then I'll review it.
"""

num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is an Even number")
else:
    print(f"{num} is a Odd number")