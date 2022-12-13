import random
from words import words
import string

"""
Function that describes the game to the user
"""


def game_instructions():
    print("----------------------------------------")
    print("\nGuess one letter (between A-Z)")
    print("\nBe careful!")
    print("\nOne wrong guess = one step closer to being hanged")
    print("\nYou have 7 chances to guess a letter in the word")
    print("\nMake sure to choose wisely")
    print("----------------------------------------")


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
        print("A-Z only please!")
        break
    else:
        return user_letter


"""
Displays the current stage of HangMan dependning on the attempts
"""


def gallows(attempts):
    if attempts == 7:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|________")
    if attempts == 6:
        print("________      ")
        print("|      |      ")
        print("|     (_)      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|________")
    if attempts == 5:
        print("________      ")
        print("|      |      ")
        print("|     (_)      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
        print("|________")
    if attempts == 4:
        print("________      ")
        print("|      |      ")
        print("|     (_)      ")
        print("|     / \     ")
        print("|             ")
        print("|             ")
        print("|________")
    if attempts == 3:
        print("________      ")
        print("|      |      ")
        print("|     (_)      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
        print("|________")
    if attempts == 2:
        print("________      ")
        print("|      |      ")
        print("|     (_)      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
        print("|________")
    if attempts == 1:
        print("________      ")
        print("|      |      ")
        print("|     (_)      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")
        print("|________")
        

"""
Main function that runs the game
"""


def play_game():
    game_instructions()
    word = chooseWord(words)
    needed_letters = len(word) * ['_']
    guessed_letters = []
    game_over = False

    attempts = 7

    while game_over is False:
        print("Your word has", len(needed_letters), "letters")
        print()
        print("You have guessed: ", guessed_letters)
        print()
        gallows(attempts)
        print()
        print("You have", attempts, "attempts left")
        print("----------------------------------------")
        
        user_guess = user_choice()
        if user_guess in guessed_letters:
            print("You have already guessed this letter")
            attempts -= 1
        elif user_guess not in word:
            print("Oops,", user_guess, "is not in the word!")
            guessed_letters.append(user_guess)
            attempts -= 1
        else:
            print("Well done,", user_guess, "is in the word")
            guessed_letters.append(user_guess)
            needed_letters = list(needed_letters)
            for i, char in enumerate(word):
                if char == user_guess:
                    needed_letters[i] = user_guess
                    print(' '.join(needed_letters))
        game_over = attempts == 0
    if game_over:
        print("You lost!")


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
            print("Welcome", user_name, "! Would you like to play?: ")
            choice = input("Y or N?: ")
            while choice not in ["y", "n", "Y", "N"]:
                print("Please choose Y or N only")
            if choice in ["Y", "y"]:
                print("Thank you,", user_name, ", the game will now begin..")
                play_game()
            elif choice in ["N", "n"]:
                print("No worries, bye!")
                quit()
        else:
            print("Please enter your name in letters only")

    
game_intro()