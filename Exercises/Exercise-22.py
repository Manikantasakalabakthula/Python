"""
Exercise 22 — Number Analyzer
Take an integer from the user and print:
- "Positive" if number > 0
- "Negative" if number < 0
- "Zero" if number == 0
Then additionally print whether the number is Even or Odd.

Use: if-elif-else and %.
"""

num=int(input("Enter an integer: "))
if num>0:
    if num%2==0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif num<0:
    if num%2==0:
        print("Negative and Even")
    else:
        print("Negative and Odd")
else:
    print("Zero")