"""
Mini Project 2 — Shopping Bill Analyzer
Create a program that takes:
- Product name
- Product price
- Quantity
Calculate:
Total = price × quantity

Then calculate:
Total / quantity
Total % quantity
Total // quantity

Also check:
- Is the total greater than or equal to 1000?
- Is the quantity greater than 1?
- Is the product name "Python" present in the product name?
Finally, create one compound expression involving arithmetic + comparison + logical operators.

Example:
Enter product name: Python Book
Enter price: 500
Enter quantity: 3

===== Shopping Bill =====
Product: Python Book
Price: 500
Quantity: 3
Total: 1500

Total / Quantity: 500.0
Total // Quantity: 500
Total % Quantity: 0

Total >= 1000: True
"""

product_name=input("Enter product name: ")
product_price=int(input("Enter product price: "))
quantity=int(input("Enter quantity: "))

total=product_price*quantity
print("===== Shopping Bill =====")
print("Product: ", product_name)
print("Price: ", product_price)
print("Quantity: ", quantity)
print("Total: ", total)

print("Total / Quantity: ", total/quantity)
print("Total // Quantity: ", total//quantity)
print("Total % Quantity: ", total%quantity)

print("Total >= 1000: ", total>=1000)
print("Quantity > 1: ", quantity>1)
print("\"Python\" in Product: ", "Python" in product_name)