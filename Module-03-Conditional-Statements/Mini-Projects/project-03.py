"""
Mini Project 3 — Menu-Based Calculator
Create a program that takes:
first_number
second_number
choice

Display this menu:
1. Addition
2. Subtraction
3. Multiplication
4. Division

Use match-case to perform the selected operation.
Requirements
- 1 → a + b
- 2 → a - b
- 3 → a * b
- 4 → a / b
- Any other choice → "Invalid Choice"
- Use round() to round the calculation result to 2 decimal places.
- Use an f-string to display the result.
Example
Enter first number: 10
Enter second number: 3
Enter choice: 1

10 + 3 = 13

Restrictions: Module 1-3 concepts only.
"""

first_number=int(input("Enter first number: "))
second_number=int(input("Enter second number: "))
choice=int(input("Enter choice: "))


match choice:
    case 1:
        print(f"{first_number} + {second_number} = {round(first_number + second_number,2)}")
    case 2:
        print(f"{first_number} - {second_number} = {round(first_number - second_number,2)}")
    case 3:
        print(f"{first_number} * {second_number} = {round(first_number * second_number,2)}")
    case 4:
        print(f"{first_number} / {second_number} = {round(first_number / second_number,2)}")
    case _:
        print("Invalid Choice")