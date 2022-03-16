'''Problem: Given a name input as a string and an age input
as an integer, return a message addressed to them that tells
them at what year they'll turn 100 years old.
Todo:
Return message if age or name is invalid.
Convert the program to a function that also takes in a number
that specifies how many copies of the generated string should
be returned.'''

# prompt the user to input name
name = input("Please enter your name:")

# prompt the user to input age
age = input("Please enter your age:")

# year equals 100 - age (converted to integer) plus the
# current year
year = (100 - int(age)) + 2022

# output string
print(f"{name} will be 100 in the year {year}")

# put it all into a function
def cent():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    repeats = input("How many times to repeat? ")
    number = (100 - int(age)) + 2022
    for i in range(0, int(repeats)):
        print(f"{name} will be 100 in {number}.")
    return print("Function complete!")