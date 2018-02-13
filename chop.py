def chop(c):
    del c[0]
    del c[-1]

letters = ['a', 'b', 'c', 'd', 'e']
chop(letters)
print(letters)