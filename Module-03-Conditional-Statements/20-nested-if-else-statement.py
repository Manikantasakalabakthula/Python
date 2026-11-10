credit_score = int(input("Enter credit score: "))

if credit_score >= 700:
    income = float(input("Enter annual income: "))
    if income >= 50000:
        print("Approved: Standard interest rate applies.")
    else:
        print("Conditional Approval: Guarantor required due to income.")
else:
    co_signer = input("Do you have a co-signer? (yes/no): ")
    if co_signer.lower() == "yes":
        print("Pending Review: Application forwarded to manual underwriting.")
    else:
        print("Rejected: Credit score does not meet minimum threshold.")