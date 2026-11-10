card_limit = 25000
transaction_amount = int(input("Enter amount: "))
if card_limit >= transaction_amount:
    print("Tranasaction Successful!")
else:
    print("Transaction Failed!")