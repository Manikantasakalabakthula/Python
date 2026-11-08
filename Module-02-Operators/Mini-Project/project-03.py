"""
Create a program that evaluates these expressions:
a = 10b = 5c = 2


Calculate and print the results of at least 5 different compound expressions using combinations of:
- +
- -
- *
- /
- //
- %
- **
- Parentheses
For each expression, calculate the answer on paper first, then run the program and verify it.

Example:
result = a + b * cprint(result)


Then create another version where parentheses change the result:
result = (a + b) * cprint(result)
"""

a = 10
b = 5
c = 2
first_result=a+b*c
second_result=a*b/c
third_result=a**b*c
fourth_result=(a+b)*c
fifth_result=(a**b)+c

print("First result: ", first_result)
print("Second result: ", second_result)
print("Third result: ", third_result)
print("Fourth result: ", fourth_result)
print("Fifth result: ", fifth_result)