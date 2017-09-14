# This game allows you to guess a number in between a chosen range by the user. You will get 
# a maximum of k(to be input by the user) chances to guess the correct number accurately.
import random

guessesTaken = 1

print('Hello! What is your name?')
myName = input()
upperrange = int(input("Choose the upper range for this game provided the lower range is zero\n"))
number = random.randint(0,upperrange )
print('Well, ' + myName + ', I am thinking of a number between 1 and '+str(upperrange))
chances = int(input("What is the maximum no. of guesses you would like to make?"))
while guessesTaken <= chances:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken-1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
print(number)
