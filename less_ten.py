'''Take a list of numbers and return all the elements that
are less than 5.
Todo:
Instead of returning elements one by one, make a new list to
return.
Write this in one line of code.
Ask the user for a number and return a list that contains
only elements from the original list that are smaller than the
number given by the user.'''

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = [a for a in nums if a < 5]
print(newlist)
newnum = input("enter a number: ")
newlist = [a for a in nums if a < int(newnum)]
print(newlist)