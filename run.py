import random
from words import words
import string

"""
Function that describes the game to the user
"""


def game_instructions():
    print("\nHow to play:")
    print("\nGuess one letter at a time")
    print("\nBe careful, there are consequences when you are incorrect")
    print("\nOne incorrect guess means one step closer to being hanged")
    print("\nYou have seven chances to guess the word")
    print("\nMake sure to choose wisely")


"""
Function that randomises a word from the list in words.py
"""


def chooseWord(words):
    word = random.choice(words)
    return word


"""
Function that will show blanks for each letter in randomised words
"""


def show_blanks(word):
    return ["_" for letter in word]


"""
Function that asks user to input a letter
"""


def user_choice():
    all_letters = set(string.ascii_letters)
    user_letter = input("Please enter a letter")
    if user_letter in all_letters:
        return user_letter
    else:
        print("Oops, letters only!")
    

"""
Main function that runs the game
"""


def play_game():
    game_intro()
    word = chooseWord(words)
    needed_letters = show_blanks(word)
    guessed_letters = set()
    remaining_letters = len(needed_letters)
    attempts = 7

    print(needed_letters)

    user_letter = user_choice()

    if user_letter in word:
        guessed_letters.add(user_letter)
        if user_letter in needed_letters:
            remaining_letters.remove(user_letter)
        else:
            attempts = attempts - 1
            print("Wrong answer, you have", attempts, "attempts left")


play_game()