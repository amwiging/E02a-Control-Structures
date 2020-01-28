#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = ''
count = 0
while (color != 'red'):
    color = input("What is my favorite color? ")
    color = color.lower().strip()
    count = count + 1               # You can also write this as count += 1
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')

print('You guessed it in {} tries!'.format(count))

#Line 13 adds a new varible of count and each time the game is looped it adds 1 to that count
#count is to allow the player at the end how many guesses it took to guess it.
#The last line shows text of how many players it took to guess it. 