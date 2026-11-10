"""
Exercise 07 — Type Conversion

Given:
num = "25"price = "99.5"


Convert them to the appropriate numeric types and print:
1. Their values
2. Their data types

Expected type information should show:
25 <class 'int'>
99.5 <class 'float'>
"""

num = "25"
price = "99.5"
converted_num=int(num)
converted_price=float(price)
print(converted_num)
print(type(converted_num))
print(converted_price)
print(type(converted_price))