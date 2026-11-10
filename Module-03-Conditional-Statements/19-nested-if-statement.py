keycard = input("Enter keycard (yes/no): ")

if keycard.lower() == "yes":
    pin = int(input("Enter PIN: "))
    if pin == 4821:
        biometrics = input("Enter biometrics (yes/no): ")
        if biometrics.lower() == "yes":
            print("Access Granted: Vault Unlocked.")