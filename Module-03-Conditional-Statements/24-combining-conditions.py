age = 20
percentage = 75
name = "Python"
marks = [75, 80, 90]

if ((age > 18 and age < 25) or
    (age >= 18 and age <= 25) and
    age == 20 and
    age != 15 and
    percentage >= 60 and
    not (percentage < 50) and
    name in "Python Programming" and
    "Java" not in name and
    75 in marks):

    print("Eligible")