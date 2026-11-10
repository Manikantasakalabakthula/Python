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