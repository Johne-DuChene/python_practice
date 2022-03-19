'''Given a list of numbers, write
one line of code that takes the list
and returns only the even elements
of that list.'''

# list of numbers
nums = [1, 2, 3, 4, 5,
    6, 7, 8, 9, 10]

# print even numbers
# item for item in numbers if item / 2
# leaves 0 behind (making it even)
print([i for i in nums if i % 2 == 0])