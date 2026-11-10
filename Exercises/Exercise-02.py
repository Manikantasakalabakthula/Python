"""
Exercise 2 - Swap Two Numbers

Task:
Write a program that takes two inputs from the user, swaps the values stored in their variables using a temporary third variable, and displays the swapped values.

Requirements:

- Prompt the user to enter two values (e.g., `first_number` and `second_number`) with explicit prompt messages.
- Swap the contents of the two variables using a temporary variable (`temp`).
- Print the value of the first variable on one line in the format: `first_number= <value>`
- Print the value of the second variable on the next line in the format: `second_number= <value>`
- Use string concatenation to display the final output labels and values.


Example:

Input:
Enter first number: 10
Enter second number: 20

Output:
first_number= 20
second_number= 10
"""

# Swap two numbers
first_number=input("Enter first number: ")
second_number=input("Enter second number: ")
temp=first_number
first_number=second_number
second_number=temp
print("first_number= "+first_number)
print("second_number= "+second_number)