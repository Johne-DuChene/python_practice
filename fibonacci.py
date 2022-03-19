'''Write a program that asks the user
how many fibonacci numbers to generate
and then generate them.
The fibonacci sequence is a sequence
of numbers where the next number
in the sequence is the sum
of the previous two numbers in
the sequence. The sequence looks like
this: 1, 1, 2, 3, 5, 8, 13...'''

# define the function
def fib(n):
    # previous number
    previous = 1
    # current number
    current = 1
    # next number
    next = 0
    # sequence
    fibo = []
    # for number in range of input
    for i in range(n):
        # next number in sequence is
        # the previous plus the current
        next = previous + current
        # append the last number
        fibo.append(previous)
        # previous number is the current
        previous = current
        # current number is the next
        current = next
    # return the sequence
    return print(fibo)
# call it on the int function which
# is called on the input function
# which takes in a number as a string
# and converts it to an int before
# running the function on it.
fib(int(input("Give me a number: ")))