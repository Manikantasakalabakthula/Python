"""
Exercise 16 — Body Mass Index (BMI) Category Evaluator

Task:
Write a program that calculates a user's Body Mass Index (BMI) from their height and weight, displays the calculated BMI value, and determines their weight category using an if-elif-else conditional ladder.

Requirements:
- Prompt the user to enter their height using: "Enter your height: "
- Convert the height input to a float.
- Prompt the user to enter their weight using: "Enter your weight: "
- Convert the weight input to a float.
- Calculate BMI using the formula: weight / height ** 2
- Print the calculated BMI preceded by the label "BMI: ".
- Use an if-elif-else ladder to evaluate the BMI against the following criteria and print the exact corresponding category:
  - bmi < 16.0 -> "Underweight (Severe thinness)"
  - bmi >= 16.0 -> "Underweight (Moderate thinness)"
  - bmi >= 17.0 -> "Underweight (Mild thinness)"
  - bmi >= 18.5 -> "Normal range"
  - bmi >= 25.0 -> "Overweight (Pre-obese)"
  - bmi >= 30.0 -> "Obese (Class I)"
  - bmi >= 35.0 -> "Obese (Class II)"
  - Otherwise -> "Obese (Class III)"

Example:
Input:
Enter your height: 1.75
Enter your weight: 45

Output:
BMI:  14.693877551020408
Underweight (Severe thinness)

Your task:
Write the Python program yourself. Don't look at the solution first.
For our modules, I'll give you 3–4 coding exercises in this format, increasing from easy → medium → challenging.
And importantly, I won't give the solution along with the question. You write the code first, then I'll review it.
"""

height=float(input("Enter your height: "))
weight=float(input("Enter your weight: "))
bmi=weight/height**2
print("BMI: ", bmi)
if bmi<16.0:
    print("Underweight (Severe thinness)")
elif bmi>=16.0:
    print("Underweight (Moderate thinness)")
elif bmi>=17.0:
    print("Underweight (Mild thinness)")
elif bmi>=18.5:
    print("Normal range")
elif bmi>=25.0:
    print("Overweight (Pre-obese)")
elif bmi>=30.0:
    print("Obese (Class I)")
elif bmi>=35.0:
    print("Obese (Class II)")
else:
    print("Obese (Class III)")