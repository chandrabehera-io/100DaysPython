import random
from replit import clear


def deal_card():
    """ Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """ Returns the score of a list of cards """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.appende(1)

    return sum(cards)


def compare_scores(user_score, computer_score):
    """ Returns the winner of the game """
    if user_score == computer_score:
        return "Its a Tie 😐"
    elif computer_score == 0:
        return "You Win 😎"
    elif user_score == 0:
        return "Computer Wins 😭"
    elif user_score > 21:
        return "You went over 21. Computer wins...!!! 😢"
    elif computer_score > 21:
        return "Computer went over 21. You Won...!!! 😍"
    elif user_score > computer_score:
        return "You  Won...!!! 😍"
    else:
        return "You loose...!!! 😢"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(
            f"Your cards are{user_cards} and current score is {user_score} .")
        print(f"Computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to deal another card? (y/n)")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card)
        computer_score = calculate_score(computer_cards)

    print(
        f"Your final hands are {user_cards} and your final score is {user_score}.")

    print(
        f"Computer's final hands are {computer_cards} and computer's final score is {computer_score}.")

    print(compare_scores(user_score, computer_score))


while input("To play again press 'y'..") == "y":
    clear()
    play_game()
