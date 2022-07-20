from art import logo, vs
from gameData import data
import random


def format_data(account):
    """Format the account into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_description} from {account_country}")


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and check if they got right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_B = random.choice(data)

while game_should_continue:
    account_A = account_B
    account_B = random.choice(data)
    if account_A == account_B:
        account_B = random.choice(data)
    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    print(f"Compare B: {format_data(account_B)}")

    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

    follower_count_A = account_A["follower_count"]
    follower_count_B = account_B["follower_count"]

    is_correct = check_answer(guess, follower_count_A, follower_count_B)
    score = 0
    if is_correct:
        score = +1
        print(f"You are right. Current Score is : {score}. ")
    else:
        game_should_continue = False
        print(f"Sorry you are wrong. Final Score is : {score}")
