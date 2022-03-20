'''Simple program that generates
a password for the user based on the
desired length input.'''

from numpy.random import choice
# takes in a number to represent
# desired length of password
def generate_password(length):
    password = []
    poss_chars_str = """A B C D E F G
        H I J K L M N O P Q R S T U V
        W X Y Z a b c d e f g h i j k
        l m n o p q r s t u v w x y z
        1 2 3 4 5 6 7 8 9 0 - + = * &
        @ ! # $ % ^ ( ) _ \ | ] [ { }
        ; : , < . > / ?"""
    for n in range(int(length)):
        password.append(choice(poss_chars_str.split()))
    return "".join(password)
des_length = input("""How many characters
    for your password?   """)
print(generate_password(des_length))