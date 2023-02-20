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

game_images = [rock, paper, scissors]
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper, of 2 for Scissors."))
print("You chose " + game_images[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose " + game_images[computer_choice])

if user_choice == computer_choice:
    print("Its a Draw!")
elif user_choice == 0 and computer_choice == 1:
    print("You Lose!")
elif user_choice == 1 and computer_choice == 0:
    print("You Win!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
elif user_choice == 1 and computer_choice == 2:
    print("You Lose!")
elif user_choice == 2 and computer_choice == 1:
    print(f"You Win!")
else:
    print("Invalid input, play again?")