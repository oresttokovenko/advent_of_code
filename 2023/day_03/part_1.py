from collections import defaultdict

# creating a 2d matrix
with open("input.txt", "r") as f:
    input = [[c for c in line.strip()] for line in f]

# test = input[0:2]
symbols = defaultdict(list)

# fetching the coordinates of every symbol
for i,j in enumerate(test):
    for ii, jj in enumerate(j):
        if not jj.isdigit() and jj != '.':
            # value is the key, x y coordinates is the value
            symbols[jj].append([i,ii])

# wip