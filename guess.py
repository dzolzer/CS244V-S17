# Guessing Game
# Author: David Zolzer
# January 26, 2017

import random

again = 'Y'

myname = input('Please enter your name: ')

while again == 'Y':
    guesses = 0   #keep track of the number of guesses
    number = random.randint(1,100)

    print("I'm thinking of a number between 1 and 100.")
    print('Can you guess the number? ')

    while guesses < 6:
        guesses += 1
        guess = eval(input('Take guess %i: ' %guesses))

        if guess < number:
            print('Your guess it too low.')
        elif guess > number:
            print('Your guess is too high.')
        else:
            break

    if guess == number:
        print('Good job, %s! You guessed the number in %i guesses.' %(myname, guesses))

    if guess != number:
        print('Nice try %s! The number I was thinking about is %i' %(myname, number))

    again = input('Play again (Y or N: )').upper()




