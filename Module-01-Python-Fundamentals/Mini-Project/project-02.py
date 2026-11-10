"""
Mini Project 2 — Simple Bill Calculator
Create a program for a small shop.

Ask the user for:
- Product name
- Product price
- Quantity
Calculate:

Total = Price × Quantity

Then display:
===== Bill =====

Product: Notebook
Price: 50
Quantity: 3
Total: 150

Requirements:
- Price should be treated as a numeric value.
- Quantity should be treated as an integer.
- Calculate the total using the variables.
- Display the result clearly.
"""

product_name=input("Enter product name: ")
product_price=int(input("Enter product price: "))
quantity=int(input("Enter quantity: "))
print("===== Bill =====")
print("Product: ", product_name)
print("Price: ", product_price)
print("Quantity: ", quantity)
print("Total: ", product_price*quantity)