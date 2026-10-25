# Jason Hoppal
# CIS256 Fall 2026
# Programming Assignment 4

import random

# Function finds all letter postitions for guessed letter. Returns letter positions in list.
def find_letter_indexes(letter_input, word):
    letter_positions = []

    index = 0

    for letter in word:
        if letter_input == letter:
            letter_positions.append(index)
        
        index += 1

    return letter_positions

# Function selects random word from word_list.
def select_random_word(word_list):
    random_number = random.randint(0, len(word_list) - 1)
    random_word = word_list[random_number]

    return random_word

# MAIN

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

if __name__ == "__main__":
    # Determine random word from word_list
    random_word = select_random_word(word_list)

    # Starts game. Prints blank word to terminal.
    print("\nWelcome to Guess The Word!")
    print("It is time to test your word guessing skills...\n")

    working_word = []

    for letter in random_word:
        print ("_", end=" ")
        working_word.append("_")

    # Initialized variables for While loop.
    word_found = False
    guess_number = 0

    # Loop continues until all letters have been found.
    while word_found == False:
        letter_guess = input("\n\nChoose a letter: ")
        guess_number += 1

        letter_positions = find_letter_indexes(letter_guess, random_word)

        for index in letter_positions:
            working_word[index] = letter_guess

        for letter in working_word:
            print(letter, end=" ")

        if "_" not in working_word:
            word_found = True

    # Prints ending message to terminal.
    print("\n\nCongratulations you have found the word!!")
    print(f"You guessed {random_word} in {guess_number} guesses.")

