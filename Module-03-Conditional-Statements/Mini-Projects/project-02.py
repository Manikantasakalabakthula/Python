"""
Mini Project 2 — Electricity Bill Calculator
Create a program that takes:
customer_name
units

Calculate the electricity bill according to these slabs:
Units	Rate
0-100	₹2 per unit
101-200	₹3 per unit
201-300	₹5 per unit
Above 300	₹7 per unit


Requirements
1. Calculate the bill using if-elif-else.
2. Add a 5% surcharge if the bill is greater than ₹1000.
3. Use round() to keep the final bill to 2 decimal places.
4. Display the customer's name and final bill using an f-string.
5. Use a ternary operator to display:
   - "High Bill" if final bill >= ₹1000
   - "Normal Bill" otherwise.
Example
For customer_name = "Mani" and units = 250:
Mani's electricity bill: ₹1250.0
High Bill

Restriction: Modules 1-3 only. No loops, functions, lists, dictionaries, etc.
"""

customer_name=input("Enter customer name: ")
units=float(input("Enter units: "))
bill=0

if units<=100:
    bill=units*2
elif units<=200:
    bill=units*3
elif units<=300:
    bill=units*5
else:
    bill=units*7

if bill>1000:
    bill*=1.05

final_bill=round(bill,2)
print(f"{customer_name}'s electricity bill: ₹{final_bill}")

result="High Bill" if final_bill>=1000 else "Normal Bill"
print(result)