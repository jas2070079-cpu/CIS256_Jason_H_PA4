# Jason Hoppal
# CIS256 Fall 2026
# Programming Assignment 4

import random

# Create word list for guessing game
word_list =[
    "football",
    "tornado",
    "mountain",
    "spaceship",
    "pineapple",
    "thunder",
    "basketball",
    "elephant",
    "volcano",
    "difficult"
]

# Determine random word from word_list
random_number = random.randint(0, len(word_list) - 1)
random_word = word_list[random_number]

print("\nWelcome to Guess The Word!")
print("It is time to test your word guessing skills...\n")

for char in random_word:
    print ("_", end=" ")


letter_guess = input("\n\nChoose a letter: ")