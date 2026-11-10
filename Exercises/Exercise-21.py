"""
Exercise 21 — Grade Checker
Write a Python program that:
- Takes marks as input.
- If marks are 90 or above → print "A Grade"
- If marks are 75 or above → print "B Grade"
- If marks are 60 or above → print "C Grade"
- Otherwise → print "Fail"
Use: if-elif-else
"""
marks=int(input("Enter marks: "))
if marks>=90:
    print("A Grade")
elif marks>=75:
    print("B Grade")
elif marks>=60:
    print("C Grade")
else:
    print("Fail")