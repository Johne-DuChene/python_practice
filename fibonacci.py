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
    return print(fibo)
fib(int(input("Give me a number: ")))