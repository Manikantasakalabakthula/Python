pizza_size=input("Enter the pizza size(small/medium/large): ")
pepperoni=input("(yes/no) for pepperoni: ")
extra_cheese=input("(yes/no) for extra cheese: ")
bill=0
if pizza_size=="small" or pizza_size=="Small":
    bill+=100
    if pepperoni=="yes" or pepperoni=="Yes":
        bill+=30
    if extra_cheese=="yes" or extra_cheese=="Yes":
        bill+=20
    print("Pizze price: ", bill)
elif pizza_size=="medium" or pizza_size=="Medium":
    bill+=200
    if pepperoni=="yes" or pepperoni=="Yes":
        bill+=50
    if extra_cheese=="yes" or extra_cheese=="Yes":
        bill+=20
    print("Pizze price: ", bill)
elif pizza_size=="large" or pizza_size=="Yes":
    bill+=300
    if pepperoni=="yes" or pepperoni=="Yes":
        bill+=50
    if extra_cheese=="yes" or extra_cheese=="Yes":
        bill+=20
    print("Pizze price: ", bill)
else:
    print("Invalid pizza size selected.")