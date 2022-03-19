'''Write a program that takes a list
and returns a new list that contains
all the same elements but with
duplicates removed.
Write two functions to do this, one
with a loop, and one with a set.'''

rand = [0, 1, 1, 2, 3, 3, 4, 4, 5]
def rem_dupes(items):
    return set(items)
print(rem_dupes(rand))

def loop_rem_dupes(items):
    newlist = []
    for i in items:
        if i not in newlist:
            newlist.append(i)
    return newlist
print(loop_rem_dupes(rand))
