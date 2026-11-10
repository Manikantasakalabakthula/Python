"""
Exercise 11 — Comparison & Logical Operators

Take a person's age and percentage as input.

Print the results of these conditions:
- Age is greater than or equal to 18
- Percentage is greater than or equal to 60
- Age is 18+ and percentage is 60+
- Age is below 18 or percentage is below 60

Example:
Enter age: 21
Enter percentage: 75

Age >= 18: True
Percentage >= 60: True
Eligible: True
Not eligible: False

Don't use if. Just print the Boolean expressions.
"""

age=int(input("Enter your age: "))
percentage=int(input("Enter your percentage: "))
print("Age >= 18:", age>=18)
print("Percentage >= 60: ", percentage>=60)
print("Eligible: ", age>=18 and percentage>=60)
print("Not eligible: ", age<18 or percentage<60)