"""
Mini Project 1 — Student Profile
Create a program that asks the user for:
- Name
- Age
- Course
- City
- Percentage
Then display a clean student profile.

Example:
===== Student Profile =====

Name: Ravi
Age: 21
Course: B.Tech
City: Hyderabad
Percentage: 82.5

Requirements:
- Use input()
- Use appropriate type conversion for numeric values
- Store values in variables
- Use print() for the output
- Don't hardcode the user's information
"""

name=input("Enter your name: ")
age=int(input("Enter your age: "))
course=input("Enter your course: ")
city=input("Enter your city: ")
percentage=input("Enter your percentage: ")
print("===== Student Profile =====")
print("Name: ", name)
print("Age: ", age)
print("Course: ", course)
print("City: ", city)
print("Percentage: ", percentage)