"""
Mini Project 1 — Student Eligibility Checker
Create a program that takes:
- Student name
- Age
- Percentage
Then calculate and print:
- Whether age is 18 or above
- Whether percentage is 60 or above
- Whether the student satisfies both conditions
- Whether the student fails either condition
Also calculate:
percentage + 5
percentage - 5
percentage * 2
percentage / 2

Example:
Enter student name: Ravi
Enter age: 21
Enter percentage: 75

===== Student Eligibility =====
Name: Ravi
Age >= 18: True
Percentage >= 60: True
Eligible: True
Not Eligible: False

Percentage + 5: 80
Percentage - 5: 70
Percentage * 2: 150
Percentage / 2: 37.5

Use: input(), type casting, arithmetic, comparison, logical operators, print().
"""

student_name=input("Enter student name: ")
age=int(input("Enter student age: "))
percentage=int(input("Enter student percentage: "))

print("===== Student Eligibility =====")
print("Name: ", student_name)
print("Age >= 18: ", age>=18)
print("Percentage >= 60: ", percentage>=60)
print("Eligible: ", age>=18 and percentage>=60)
print("Not Eligible: ", age<18 or percentage<60)

print("Percentage + 5: ", percentage+5)
print("Percentage - 5: ", percentage-5)
print("Percentage * 2: ", percentage*2)
print("Percentage / 2: ", percentage/2)