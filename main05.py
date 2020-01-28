#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#I expect it to format the players response to all lower case letters so that in any way you type red it will be right
#This is solving the problem of the player using a different scheme of capital letters
#When adding spaces it is counted as incorrect