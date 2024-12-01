from itertools import islice
from pathlib import Path

total_distance = 0

p = Path("input.txt").read_text().split()

# splitting into two lists and sorting in ascending order
list_1 = sorted([int(i) for i in islice(p, 0, None, 2)])
list_2 = sorted([int(i) for i in islice(p, 1, None, 2)])

for i, j in zip(list_1, list_2, strict=False):
    total_distance += abs(i - j)

print(total_distance)
