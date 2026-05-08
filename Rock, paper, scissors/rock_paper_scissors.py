import random

rock = '''
    ______
---'   ____)
      (_____)
      (_____)
      (____)
---.(___)
'''

paper = '''
     _____
---'   ____)__
          ______)
          _______)
         _______)
---.________)
'''

scissors = '''

---'_________
          ______)__
       __________)
      (____)
---.(___)
'''

player_input = input("Welcome to the Rock, Paper, Scissors game!\n"
                     "Type what you want to play here: \n")

options_list = [rock, paper, scissors]

comp_pick = random.choice(options_list)

if player_input == rock and comp_pick == rock:
    print()