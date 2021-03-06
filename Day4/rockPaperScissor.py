# rock paper scissors game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(
    input("What do you choose? Type 0 for ROCK, 1 for PAPER and 2 for SCISSORS\n"))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)


computer_choice = random.randint(0, 2)
print(f"COMPUTER choose : {computer_choice} \n")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)


# result
if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!") 
elif choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and choice == 2:
  print("You lose")
elif computer_choice > choice:
  print("You lose")
elif choice > computer_choice:
  print("You win!")
elif computer_choice == choice:
  print("It's a draw")
