'''Write a function that takes an
ordered list of numbers and another
number. The function decides whether
or not the given number is inside
the list and returns an appropriate
boolean.'''

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def check(number):
    if number in nums:
        return True
    else:
        return False
print(check(int(input("Give me a number: "))))