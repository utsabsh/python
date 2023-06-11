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
game_image =[rock,paper,scissors]
computerchoice = random.randint(0,2)

human_choice = int(input("what do you choose? type 0 for rock,1 for paper, 2 for scissors\n"))
if 3>= human_choice <=0:
    print(game_image[human_choice])
print(f"computer choose: {computerchoice}")
if 3>= computerchoice <=0:
    print(game_image[computerchoice])
if human_choice == 0 and computerchoice == 0:
    print("draw!")
elif human_choice == 0 and computerchoice == 1:
    print("you loose!!")
elif human_choice == 0 and computerchoice == 2:
    print("you win!!")
elif human_choice == 1 and computerchoice == 0:
    print("you win!")
elif human_choice == 1 and computerchoice == 1:
    print("draw!!")
elif human_choice == 1 and computerchoice == 2:
    print("you loose!!")
elif human_choice == 2 and computerchoice == 0:
    print("you loose!")
elif human_choice == 2 and computerchoice == 1:
    print("win!!")
elif human_choice == 2 and computerchoice == 2:
    print("draw!!")
else:
    print("invaild input")