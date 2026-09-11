import random

word_list = ["baboon", "camel", "monkey", "cotton", "dream", "day", "code", "flashlight", "light", "doom", "siren", "fight", "prison", "moon", "sun", "devil", "demon", "soda", "flower", "project", "life", "jump", "cake", "lie", "game", "draw", "drawing", "pie", "cat", "dog", "bird", "rat", "crawl", "sleep"]

#Randomly choose a word:
for word in word_list:
    chosen_word = word
print(chosen_word)

print("Welcome to Hangman!")
print("Let's guess some words!")

guess = input("Guess a letter: ").lower()

#gjkfhdlxrtuiephøgsn hbjfg,dkkm cvnn
for guessed_word in chosen_word:
    if guess == chosen_word:
        print("Right")
    else:
        print("Wrong")