p1 = input("input a number:\
    Rock: 1\
    Paper: 2\
    Scissors: 3   ")
p2 = input("input a number:\
    Rock: 1\
    Paper: 2\
    Scissors: 3   ")

# if both are the same, it's a draw
if p1 == p2:
    print("Draw!")

if p1 == "1":
    if p2 == "2":
        print("P2 wins!")
    elif p2 == "3":
        print("P1 wins!")

if p1 == "2":
    if p2 == "1":
        print("P1 wins!")
    elif p2 == "3":
        print("P2 wins!")

if p1 == "3":
    if p2 == "1":
        print("P2 wins!")
    elif p2 == "2":
        print("P1 wins!")