import random
from words import words
import string

"""
Function that describes the game to the user
"""

def game_intro():
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
Main function that runs the game
"""


def play_game():
    game_intro()
    word = chooseWord(words)
    
play_game()