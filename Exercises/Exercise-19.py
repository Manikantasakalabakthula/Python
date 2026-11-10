"""
Exercise 19 — Love Calculator

Task:
Write a program that tests the compatibility between two people by calculating a "Love Score" based on how frequently the letters in the words "TRUE" and "LOVE" occur in their combined names, and outputs a personalized message based on the final score.

Requirements:
- Prompt the user to enter their name using: "Enter your name: " and convert it to lowercase.
- Prompt the user to enter their partner's name using: "Enter your partner name: " and convert it to lowercase.
- Combine both names into a single string.
- Count the occurrences of each letter in the word "TRUE" ('t', 'r', 'u', 'e') in the combined names and sum them up to form the first digit.
- Count the occurrences of each letter in the word "LOVE" ('l', 'o', 'v', 'e') in the combined names and sum them up to form the second digit.
- Concatenate the two counts as strings and convert the result into a two-digit integer (`true_love`).
- Evaluate the score using conditional statements:
  - If the score is less than 10 or greater than 90:
    Print: "Your score is {true_love}% and you go together like Coke and Mentos"
  - If the score is between 40 and 50 (inclusive):
    Print: "Your score is {true_love}% and you are all right together"
  - Otherwise:
    Print: "Your score is {true_love}%"

Example:
Input:
Enter your name: David
Enter your partner name: Jennifer

Output:
Your score is 44% and you are all right together

Your task:
Write the Python program yourself. Don't look at the solution first.
For our modules, I'll give you 3–4 coding exercises in this format, increasing from easy → medium → challenging.
And importantly, I won't give the solution along with the question. You write the code first, then I'll review it.
"""

my_name = input("Enter your name: ").lower()
partner_name = input("Enter your partner name: ").lower()
name = my_name + partner_name

t  =  name.count("t")
r  =  name.count("r")
u = name.count("u")
e = name.count("e")
true = str(t + r + u + e)

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
love = str(l + o + v + e)

true_love = int(true + love)
if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}% and you go together like Coke and Mentos")
elif 40<=true_love<=50:
    print(f"Your score is {true_love}% and you are all right together")
else:
    print(f"Your score is {true_love}%")