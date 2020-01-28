#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red' or color == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#Now the options for "color" have expanded and you no longer have to have it capitalized
#Now you wont be wrong when not capitalizing
#when not using "Red" or "red" exactly it is seen as incorrect