#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = ''
while (color != 'red'):
    color = input("What is my favorite color? ")
    color = color.lower().strip()
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')

# i think line 9 is looping the code so that the player can guess again if theyre wrong
#lines 10-17 are indented so that they happen after line 9, not at the same time
