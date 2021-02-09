# number guessing game

import random

print('set the lower bound:')
lowerBound = int(input())
print('set the higher bound:')
higherBound = int(input())

guesses = 0

number = random.randint(lowerBound, higherBound)

for guesses in range (5):
    print('Guess the number: ')
    guess = int(input())

    if guess < number:
        print('Try a higher number')

    if guess > number:
        print('Try a lower number')

    if guess == number:
        print(f'Your guess is correct! it took you ',guesses + 1 ,' guesses')
        break

if guess != number:
    print(f'The correct number was: ', number)
