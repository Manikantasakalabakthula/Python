"""
Exercise 14 — Life in Weeks Calculator

Task:
Write a program that takes your current age as input and calculates how many days, weeks, and months you have left if you live until 90 years old, displaying the result using an f-string.

Requirements:
- Prompt the user to enter their current age using: "Enter your current age: "
- Convert the age input to an integer.
- Calculate the remaining years assuming a maximum lifespan of 90 years (`90 - age`).
- Calculate the remaining time based on:
  - 365 days in a year
  - 52 weeks in a year
  - 12 months in a year
- Print the result in the exact format:
  `You have {days_left} days, {weeks_left} weeks and {months_left} months left`

Example:
Input:
Enter your current age: 20

Output:
You have 25550 days, 3640 weeks and 840 months left

Your task:
Write the Python program yourself. Don't look at the solution first.
For our modules, I'll give you 3–4 coding exercises in this format, increasing from easy → medium → challenging.
And importantly, I won't give the solution along with the question. You write the code first, then I'll review it.
"""

age=int(input("Enter your current age: "))
years_left=90-age

days_left=years_left*365
weeks_left=years_left*52
months_left=years_left*12
print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")