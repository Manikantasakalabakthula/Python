"""
Exercise 18 — Pizza Order Bill Calculator

Task:
Write a program that calculates the final bill for a customer's pizza order based on the chosen pizza size and optional add-ons (pepperoni and extra cheese) using conditional statements.

Requirements:
- Prompt the user to enter the pizza size using: "Enter the pizza size(small/medium/large): "
- Prompt the user to specify if they want pepperoni using: "(yes/no) for pepperoni: "
- Prompt the user to specify if they want extra cheese using: "(yes/no) for extra cheese: "
- Base pricing:
  - Small pizza: 100
  - Medium pizza: 200
  - Large pizza: 300
- Add-on pricing:
  - Pepperoni for small pizza: +30
  - Pepperoni for medium or large pizza: +50
  - Extra cheese for any pizza size: +20
- Handle both lowercase and capitalized user inputs (e.g., "small" or "Small", "yes" or "Yes").
- Display the final bill using the format: "Pizze price:  <bill>"
- If an invalid size is entered, display: "Invalid pizza size selected."

Example:
Input:
Enter the pizza size(small/medium/large): small
(yes/no) for pepperoni: yes
(yes/no) for extra cheese: no

Output:
Pizze price:  130

Your task:
Write the Python program yourself. Don't look at the solution first.
For our modules, I'll give you 3–4 coding exercises in this format, increasing from easy → medium → challenging.
And importantly, I won't give the solution along with the question. You write the code first, then I'll review it.
"""

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