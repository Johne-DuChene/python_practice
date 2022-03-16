'''Create a program that asks for a number and returns a list
of all of its divisors.'''

# instantiates the list
num_list = []
# prompts the input of a number
number = input("Please give me a number: ")
# inputs are strings by default, so I convert it to an int
number = int(number)
# for each number in the range of 1 and the target
for i in range(1, number):
    # if the remainder of the target divided by the current
    # number is 0 (divides evenly):
    if number % i == 0:
        # add the number into the number list
        num_list.append(i)
# return the number list to the user
print(num_list)