import random
from words import words
import string

#return a valid word which doesnt contain spaces or dashes 
def valid_words(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = valid_words(words)
    #set() method is used to convert to sequence of iterable elements with distinct elements
    word_letters = set(word)
    #aplhabet will store every upper case letter
    alphabet = set(string.ascii_uppercase)
    #to store what we have already guessed
    used_letters = set()

    lives = 6

    while len(word_letters)>0 and lives>0:
        #join letters by ' ' 
        print('You have ',lives,' lives letf and you have used these letters: ',' '.join(used_letters))

        #what current word is
        word_list = [alph if alph in used_letters else '_' for alph in  word]
        print('\nCurrent word: ',' '.join(word_list))


        letter = input("Guess a Letter ").upper()
        if letter in alphabet - used_letters:
            used_letters.add(letter)
            if letter in word_letters:
                word_letters.remove(letter)
            else:
                lives = lives-1;
                print("You lost a live")


        elif letter in used_letters:
            print("\nYou have already gussed this alphabet, Please try again!")

        else:
            print("\nInvalid Character")
            
    if(lives==0):
        print("Sorry, you died !!")

    print(f"\nThe word is {word}")

print("\n\t\tWelcome To Hangman\n")
hangman()     
