'''This program takes a list of nums
and makes a new list of only the
first and last elements of the
input list.'''

# sample list
a = [5, 10, 15, 20, 25]
# define the function
# takes in a list of numbers
def ends(nums):
    # returns a list composed of
    # the first and last elements
    # of the input list
    return print([nums[0], nums[-1]])
# call the function on the sample
# list.
ends(a)