"""
Exercise 24 — Student Result
Take:
student_name
marks

Then:
- Calculate marks + 5
- Round the result to 2 decimal places
- Use an f-string to display the student's name and updated marks.
- If the updated marks are 60 or above, print "Eligible"
- Otherwise print "Not Eligible"
Example format:
Mani scored 85.0 after bonus
Eligible

Use: round(), f-string, if-else.
"""

student_name=input("Enter student name: ")
marks=float(input("Enter student marks: "))
marks+=5
result=round(marks,2)
print(f"{student_name} scored {result} after bonus")
if result>=60:
    print("Eligible")
else:
    print("Not Eligible")