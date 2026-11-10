"""
Exercise 13 — Operator Precedence Challenge
Write a program that evaluates this expression:
result = 10 + 5 * 2 ** 2 - 8 // 3


Print result.
"""

result = 10 + 5 * 2 ** 2 - 8 // 3 # 28
print(result)
update_result=10 + 5 * (2 ** 2) - 8 // 3 #28
print(update_result)
update_result_1=10 + 5 * 2 ** 2 - (8 // 3) #28
print(update_result_1)
update_result_2=(10 + 5) * 2 ** 2 - 8 // 3 #58
print(update_result_2)