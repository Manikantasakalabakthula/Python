"""
Exercise 17 — Leap Year Checker

Task:
Write a program that takes a year as input and determines whether it is a leap year or not using nested if-else statements based on standard calendar leap year rules.

Requirements:
- Prompt the user to enter a year using: "Enter year: "
- Convert the entered input to an integer.
- Implement the leap year logic using nested if-else conditions:
  - Check if the year is evenly divisible by 4.
  - If divisible by 4, check if it is divisible by 100.
  - If divisible by 100, check if it is divisible by 400 to qualify as a leap year.
  - If divisible by 4 but not by 100, it is a leap year.
  - If not divisible by 4, it is not a leap year.
- Print "It is a leap year" or "It is not a leap year" based on the evaluation.

Example:
Input:
Enter year: 2000

Output:
It is a leap year

Your task:
Write the Python program yourself. Don't look at the solution first.
For our modules, I'll give you 3–4 coding exercises in this format, increasing from easy → medium → challenging.
And importantly, I won't give the solution along with the question. You write the code first, then I'll review it.
"""

year=int(input("Enter year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")