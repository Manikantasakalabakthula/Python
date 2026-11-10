"""
Exercise 21 — Login Checker
Write a program that takes:
username
password

Rules:
- username must be "admin"
- password must be "python123"
- If both are correct → "Login Successful"
- Otherwise → "Invalid Credentials"
Use: if-else + and
"""

username=input("Enter your usename: ")
password=input("Enter your password: ")
if username=="admin" and password=="python123":
    print("Login Successful")
else:
    print("Invalid Credentials")