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

images = [rock, paper, scissors]

player1_choice = int(input("What do you choose? 0 for rock, 1 for paper, or 2 for scissors: "))
print(player1_choice)
if player1_choice >=3 or player1_choice < 0:
    print("You chose an invalid option and therefore you lose!!!")
else:
    print(images[player1_choice])

    computer_choice = random.randint(0,2)
    print(f"Computer chose: {computer_choice}")
    print(images[computer_choice])


    if computer_choice == player1_choice:
        print("It's a draw")
    #computer chooses rock and player choose paper = you win
    elif computer_choice == 0 and player1_choice == 1:
        print("You Win")
    #computer chooses rock and player choose scissors = you lose
    elif computer_choice == 0 and player1_choice == 2:
        print("You Lose")
    #computer chooses paper and player choose rock = you lose
    elif computer_choice == 1 and player1_choice == 0:
        print("You Lose")
    #computer chooses paper and player chooses scissors
    elif computer_choice == 1 and player1_choice == 2:
        print("You Win")
    #computer chooses scissors and player chooses rock
    elif computer_choice == 2 and player1_choice == 0:
        print("You Win")
    #computer chooses scissors and player chooses paper
    else:
        print("You Lose")
