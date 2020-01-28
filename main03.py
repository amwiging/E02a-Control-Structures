#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#Lines 9-12 are different in that it is now readin the input and responding if you were to give the correct answer.
#Lines 10 and 12 are indented so that "if" is correct that line 10 comes after and the same principle it it wasnt correct
#if it is not capital than it gives you the "sorry" message.
#"color" is caps sensitive and needs to be exact in order to get it correct