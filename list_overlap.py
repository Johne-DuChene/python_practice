'''Write a program that returns a list that contains common
elements between two input lists without duplicates. Ensure
it works for lists of two different sizes.'''

# list of random numbers
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# newlist:
    # sets ensure unique values
    # evaluations for each number in a if it's also in b
newlist = list(set([i for i in a if i in b]))
# return the new list
print(newlist)