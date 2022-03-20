'''Write a program using functions
that takes in a long string containing
multiple words, and then print
back that string but with the words
reversed.'''

# define function
def strings(input):
    # split input on whitespace
    strlist = input.split()
    # make an empty list to hold words
    newlist = []
    # make an iterator to represent
    # index in for loop
    iterator = -1
    # for item in list of strings: 
    for i in strlist:
        newlist.append(strlist[iterator])
        iterator -= 1
    return " ".join(newlist)
userinput = input("Give me a string: ")
print(strings(userinput))