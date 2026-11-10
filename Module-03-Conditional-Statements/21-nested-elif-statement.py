zone = input("Enter destination zone (Domestic/International): ")

if zone.lower() == "domestic":
    weight = float(input("Enter package weight (kg): "))
    if weight <= 2.0:
        print("Shipping cost is $5")
    elif weight <= 10.0:
        print("Shipping cost is $12")
    else:
        print("Shipping cost is $25")
elif zone.lower() == "international":
    speed = input("Enter shipping speed (Economy/Standard/Express): ")
    if speed.lower() == "economy":
        print("Shipping cost is $20")
    elif speed.lower() == "standard":
        print("Shipping cost is $45")
    elif speed.lower() == "express":
        print("Shipping cost is $80")
    else:
        print("Invalid shipping speed selected.")
else:
    print("Unsupported destination zone.")