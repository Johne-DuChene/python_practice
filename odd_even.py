"""This program will take in a number, then tell the user
if the number is odd or even.
Todo:
Get the basic function up and running. Print a message.
If the number is a multiple of 4, print a different message.
Ask the user for two numbers: one to check and
one to divide by. If the two divide evenly, tell that to the
user. If not, print a different message."""

num = input("Give me a number: ")
if int(num) % 2 == 0:
    print("This number is even.")
else:
    print("This number is not even.")

# dividend function
div = input("Give me a number: ")
inp = input("Give me a number to divide by: ")
if int(div) % int(inp) == 0:
    print("Divides evenly")
elif int(div) % int(inp) != 0:
    print("Doesn't divide evenly")
print(int(div) % int(inp))