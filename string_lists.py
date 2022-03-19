'''ask the user for a string and
print out whether the string is a
palindrome or not.'''

# prompt user for a string
pal = input("Give me a string: ")
# if string = string backwards"
if pal == pal[::-1]:
    # it's a palindrome
    print("This is a palindrome.")
# if it's not:
else:
    # then it isn't a palindrome
    print("this is not a palindrome")