from numpy.random import choice
number = choice([1, 2, 3, 4,
    5, 6, 7, 8, 9])
i = 0
while i != number:
    i = int(input("Guess a number between 1 and 9: "))
    if i == number:
        break
print("You win!")