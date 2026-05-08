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
                               "Type what you want to play here: ")

options_list = ["rock", "paper", "scissors"]

comp_pick = random.choice(options_list)

if player_input == "rock" and comp_pick == "rock":
    print(f"Player choose rock: \n {rock}")
    print(f"Computer choose rock: \n {rock}")
    print("Its a tie!")
elif player_input == "rock" and comp_pick == "paper":
    print(f"Player choose rock: \n {rock}")
    print(f"Computer choose paper: \n {paper}")
    print("Computer wins!")
elif player_input == "rock" and comp_pick == "scissors":
    print(f"Player choose rock: \n {rock}")
    print(f"Computer choose scissors: \n {scissors}")
    print("You win!")
elif player_input == "paper" and comp_pick == "rock":
    print(f"Player choose paper: \n {paper}")
    print(f"Computer choose rock: \n {rock}")
    print("You win!")
elif player_input == "paper" and comp_pick == "scissors":
    print(f"Player choose paper: \n {paper}")
    print(f"Computer choose scissors: \n {scissors}")
    print("Computer wins!")
elif player_input == "paper" and comp_pick == "paper":
    print(f"Player choose paper: \n {paper}")
    print(f"Computer choose paper: \n {paper}")
    print("Its a tie!")
elif player_input == "scissors" and comp_pick == "rock":
    print(f"Player choose scissors: \n {scissors}")
    print(f"Computer choose rock: \n {rock}")
    print("Computer wins!")
elif player_input == "scissors" and comp_pick == "paper":
    print(f"Player choose scissors: \n {scissors}")
    print(f"Computer choose paper: \n {paper}")
    print("You win!")
elif player_input == "scissors" and comp_pick == "scissors":
    print(f"Player choose scissors: \n {scissors}")
    print(f"Computer choose rock: \n {rock}")
    print("Computer wins!")
else:
    print("Invalid input. You have to type 'Rock' 'Paper' or 'Scissors' ")