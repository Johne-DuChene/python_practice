'''Take two lists and return a list
that contains only common elements
between the original 2 without
duplication. Use at least one list
comprehension for this.'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(set([i for i in a if i in b]))