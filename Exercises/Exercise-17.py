height=float(input("Enter your height: "))
weight=float(input("Enter your weight: "))
bmi=weight/height**2
print("BMI: ", bmi)
if bmi<16.0:
    print("Underweight (Severe thinness)")
elif bmi>=16.0:
    print("Underweight (Moderate thinness)")
elif bmi>=17.0:
    print("Underweight (Mild thinness)")
elif bmi>=18.5:
    print("Normal range")
elif bmi>=25.0:
    print("Overweight (Pre-obese)")
elif bmi>=30.0:
    print("Obese (Class I)")
elif bmi>=35.0:
    print("Obese (Class II)")
else:
    print("Obese (Class III)")