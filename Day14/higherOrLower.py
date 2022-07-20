from art import logo, vs
from gameData import data
import random
print(logo)

# pull out random account from list
# nicely formatted data
randNum_A = random.randint(1, 50)
follower_A = data[randNum_A]["follower_count"]
name_A = data[randNum_A]["name"]
country_A = data[randNum_A]["country"]
description_A = data[randNum_A]["description"]
print(
    f"Compare A: {name_A}, a {description_A} from {country_A} has {follower_A} million followers.")
print(vs)
randNum_B = random.randint(1, 50)
follower_B = data[randNum_B]["follower_count"]
name_B = data[randNum_B]["name"]
country_B = data[randNum_B]["country"]
description_B = data[randNum_B]["description"]
print(
    f"Compare B: {name_B}, a {description_B} from {country_B} has {follower_B} million followers.")

# ask user for guess
# after guessing check the answer if its correct
score = 0
guess_by_user = input("Type 'A' or 'B' : ")
if guess_by_user == "A":
    if follower_A > follower_B:
        print(f"You are correct!{name_A} has {follower_A} million followers.")
        score += 1
    else:
        print(
            f"You are wrong! {name_A} has only {follower_A} million followers.")
elif guess_by_user == "B":
    if follower_B > follower_A:
        print(f"You are correct!{name_B} has {follower_B} million followers.")
        score += 1
    else:
        print(
            f"You are wrong! {name_B} has only {follower_B} million followers.")
# tracking score
print(f"Your score is {score}")
# while user is right, repeat
#  new A = correct answer B= new personality


# screen is cleared
