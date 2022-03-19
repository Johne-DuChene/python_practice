'''Create a random number
guessing game.'''

# import choice from the
# numpy.random module.
from numpy.random import choice

# choice function and possible nums
number = choice([1, 2, 3, 4,
    5, 6, 7, 8, 9])
# instantiate guess variable
i = 0
# if i isn't number
while i != number:
    # i is the user's guess
    i = int(input("Guess a number between 1 and 9: "))
    # break loop if i is the
    # generated number
    if i == number:
        break
# print "you win!" when while
# loop is broken.
print("You win!")