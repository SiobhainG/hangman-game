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
Function that asks user to input a letter
"""


def user_choice():
    all_letters = set(string.ascii_letters)
    user_letter = input("Please enter a letter: ")
    while len(user_letter) > 1 or user_letter not in all_letters:
        print("Single letters only please!")
        break
    else:
        return user_letter


"""
Main function that runs the game
"""


def play_game():
    game_instructions()
    word = chooseWord(words)
    needed_letters = len(word) * ['_']
    guessed_letters = []
    gameOver = False

    attempts = 7

    while attempts > 0 and gameOver is False:
        print("You have guessed", guessed_letters)
        print(needed_letters)
        user_guess = user_choice()
        if user_guess in guessed_letters:
            print("You have already guessed this letter")
        elif user_guess not in word:
            guessed_letters.append(user_guess)
            attempts -= 1
        else:
            print("Well done, that is in the word")
            




        

    


"""
Asks the user for their name & asks if they want to play.
"""


def game_intro():
    while True:
        global user_name
        print("Welcome to...")
        print("""                                          
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                    |___/""")
        user_name = input("Please enter your name: ")
        if user_name.isalpha():
            print("Welcome,", user_name, "Would you like to play?: ")
            choice = input("Y or N?")
            while choice not in ["y", "n", "Y", "N"]:
                print("Please choose Y or N only")
            if choice in ["Y", "y"]:
                print("Thank you,", user_name, "the game will now begin..")
                play_game()
            elif choice in ["N", "n"]:
                print("No worries, bye!")
                quit()
        else:
            print("Please enter your name in letters only")

    
game_intro()