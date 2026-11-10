"""
Exercise 09 — Body Mass Index (BMI) Calculator

Task:
Write a program that calculates a user's Body Mass Index (BMI) 
using their weight (in kilograms) and height (in meters).

Requirements:
- Prompt the user to enter their weight using: "Enter your weight: "
- Convert the entered weight to an integer.
- Prompt the user to enter their height using: "Enter your height: "
- Convert the entered height to a floating-point number.
- Calculate the BMI using the formula: weight / (height ** 2)
- Print the calculated BMI preceded by the label "BMI: ".

Example:
Input:
Enter your weight: 70
Enter your height: 1.75

Output:
BMI:  22.857142857142858

Your task:
Write the Python program yourself. Don't look at the solution first.
For our modules, I'll give you 3–4 coding exercises in this format, increasing from easy → medium → challenging.
And importantly, I won't give the solution along with the question. You write the code first, then I'll review it.
"""

weight=int(input("Enter your weight: "))
height=float(input("Enter your height: "))
bmi=weight/(height**2)
print("BMI: ", bmi)