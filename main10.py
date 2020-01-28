#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') #This line just shows text saying greetings
colors = ['red','orange','yellow','green','blue','violet','purple'] #this line determines the color varibles that can be chosen
play_again = '' #This line repeats the loop if the player wants to play again
best_count = sys.maxsize            # the biggest number # i have no idea what this does

while (play_again != 'n' and play_again != 'no'): #this line says if they tyoe n or no when asked if they want to play again it will work
    match_color = random.choice(colors) #this line chooses a random color from the choices above
    count = 0 # this line sets the number of guesses to 0
    color = '' # i dont really know what this does
    while (color != match_color): #not sure
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line #this line asks the palyer tp guess the color
        color = color.lower().strip() #this line formats the response so that it can be read lowercase and anywhere on the line
        count += 1 #this line adds 1 to the numbner of guesses 
        if (color == match_color): # this says if the color matches the guess to say correct
            print('Correct!') # this is the line that says correct
        else: # if it is not the correct color that it willshow the next line
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # this says that you got it wrong and how many guesses you have
    
    print('\nYou guessed it in {} tries!'.format(count)) # if its right it will say that you guessed it in count many tries

    if (count < best_count): #this says if the count from a round is less than best count then to do the next lines
        print('This was your best guess so far!') # this says that this is you best score so far
        best_count = count # this coverts best_count into the current count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #this asks if you want to play again and formats the text

print('Thanks for playing!') #once you quit this says thanks for playing