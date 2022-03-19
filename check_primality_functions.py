'''In this program, ask a user for
a number and determine if it's
prime or not.'''

# user input is turned into an int
num = int(input("Gimme a number: "))
# instantiate counter
counter = 0
# for number in the range of
# 2 and our number (the upper value
# of range is exclusionary, hence the
# + 1)
for i in range(2, num + 1):
    # if the input divided by the
    # current number has a remainder
    # of 0 (meaning it has a divisor)
    if num % i == 0:
        # break the loop
        break
    # if not:
    else:
        # add 1 to the counter var
        counter += 1
# if the counter equals the input minus
# 2 (due to the exclusion of 1 and
# the exclusionary nature of range)
if counter == num - 2:
    # it's a prime number!
    print("This is a prime number!")
# if counter isn't equal to num -2:
else:
    # it must then have a divisor,
    # meaning it isn't a prime num!
    print("This is not a prime number!")