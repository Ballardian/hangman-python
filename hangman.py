""" Hangman in Python """

import os
import random
import sys

# make list of words
words = [
    "thedarktower",
    "northernlights",
    "mortalengines",
    "thebookthief",
    "thenameofthewind",
    "thegoneawayworld"
]

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def draw(bad_guesses, good_guesses, secret_word):
    clear()
    
    print("Strikes: {}/7".format(len(bad_guesses)))
    print("")
    
    for letter in bad_guesses:
        print(letter, end= "  ")
    print("\n\n")
    
    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print("")
    print("")
    
    
def get_guess(bad_guesses, good_guesses):
    while True:
        guess = input("Guess as letter... ").lower()
            
        if len(guess) != 1:
            print("You can only guess a single letter!")
            #continue
        elif guess in bad_guesses or guess in good_guesses:
            print("you have already guessed that letter!")
            #continue
        elif not guess.isalpha():
            print("You can only guess a letter!")
            #continue
        else:
            return guess

        
def play_hangman(done):
    clear()
    secret_word = random.choice(words)
    bad_guesses = set()
    good_guesses = set()
    word_set = set(secret_word)
    
    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses | good_guesses)
        
        if guess in word_set:
            good_guesses.add(guess)
            if not word_set.symetric_difference(good_guesses):
                print("You win! The word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.add(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost!")
                print("My secret word was {}".format(secret_word))
                done = True
                
        if done:
            play_again = input("Play again? Y/n ").lower()
            if play_again != "n":
                return play_hangman(done=False)
            else:
                print("Goodbye")
                sys.exit()

def welcome():
    start = input("Press enter to start or Q to quit").lower()
    if start == "q":
        print("Bye")
        sys.exit()
    else:
        return True
    
print("Welcome to Hangman")
    
done=False

while True:
    clear()
    welcome()
    play_hangman(done)
