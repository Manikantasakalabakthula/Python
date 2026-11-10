"""
Mini Project 1 — Student Result Analyzer
Create a program that takes:
student_name
marks

Requirements
1. Convert marks to float.
2. Add 5 bonus marks.
3. Round the final marks to 2 decimal places.
4. Display the result using an f-string.
Then determine the grade:
- 90+ → "A Grade"
- 75-89.99 → "B Grade"
- 60-74.99 → "C Grade"
- Below 60 → "Fail"
Then determine eligibility:
- Final marks >= 60 → "Eligible"
- Otherwise → "Not Eligible"
Restrictions
Use only concepts from Modules 1-3.

Don't use loops, functions, lists, dictionaries, etc.
Example
Enter student name: Mani
Enter marks: 72.5

Mani scored 77.5 after bonus
B Grade
Eligible
"""

student_name=input("Enter student name: ")
marks=float(input("Enter student marks: "))
marks+=5
result=round(marks,2)

print(f"{student_name} scored {result} after bonus")

if result>=90:
    print("A Grade")
elif result>=75:
    print("B Grade")
elif result>=60:
    print("C Grade")
else:
    print("Fail")

if result>=60:
    print("Eligible")
else:
    print("Not Eligible")
