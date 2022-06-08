# logical operator
# and or not

print("Welcome o the Love calculator")
name1 = input("What is your name ?\n")
name2 = input("What is their name ?\n")

combined_string = name1+name2
lowercase_str = combined_string.lower()

t = lowercase_str.count("t")
r = lowercase_str.count("r")
u = lowercase_str.count("u")
e = lowercase_str.count("e")

tru = t+r+u+e

l = lowercase_str.count("l")
o = lowercase_str.count("o")
v = lowercase_str.count("v")
e = lowercase_str.count("e")

love = l+o+v+e

lovescore = int(str(tru)+str(love))
# print(lovescore)


if (lovescore < 10) or (lovescore > 90):
    print(
        f"The lovescore is {lovescore}, you go together like coke and mentos")
elif (lovescore >= 40) and (lovescore <= 50):
    print(f"Your score is {lovescore}, you are alright together")
else:
    print(f"Your score is {lovescore}")
