import random

print("Welcome to the number Guessing Game...!!!")
print("Guess a number between 1 and 100: ")
difficulty_level = input("Choose a difficulty level: 'easy' or 'hard' :")

if difficulty_level == "easy":
    guess = 10
elif difficulty_level == "hard":
    guess = 5
else:
    print("Invalid input")
    exit()

actual_number = random.randint(1, 100)

while guess > 0:
    guessed_number = int(input("Make a guess: "))
    guess -= 1
    if guessed_number == actual_number:
        print("You guessed the number correctly.")
        break
    elif guessed_number > actual_number:
        print("Your guess is too high")
        print(f"You have {guess} attempts to guess the number.")
    elif guessed_number < actual_number:
        print("Your guess is too low")
        print(f"You have {guess} attempts to guess the number.")

if guess == 0:
    print("You ran out of guesses...!!!")
    print(f"The number was {actual_number}")
