


#This is a guess number game

import random

guessestaken = 0

print('Hello, What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20')

for guessestaken in range(6):
    print('take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    guessestaken =str(guessestaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessestaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
    
