#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower().strip() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#line 9 now says .strip after .lower
#i think it is allowing the player to put "red" anywhere on the line 
# i couldnt find anything that can break this logic