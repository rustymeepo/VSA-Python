# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
turns = 1
count = 0
import random
number = random.randint(1,20)
print 'i have chosen a number between 1 and 20. Do you think you can guess it in ' + str(random.randint(2,10)) + ' guesses? Give it your best shot!'
player = int(raw_input())
while count == 0:
    turns = turns + 1
    insult = random.randint(1,10)
    if number < player :
        print 'lower!'
        print 'Try Again'
        player = int(raw_input())
    if number > player :
        print 'higher!'
        print 'Try Again!'
        player = int(raw_input())
    if number == player:
        print 'i have been defeated! good job! you guessed my number in ' + str(turns) + ' guesses!'
        break