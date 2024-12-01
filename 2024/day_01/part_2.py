from collections import Counter
from itertools import islice
from pathlib import Path

p = Path("input.txt").read_text().split()

# splitting into two lists
l = [int(i) for i in islice(p, 0, None, 2)]
r = [int(i) for i in islice(p, 1, None, 2)]

# counting occurrences of elements in r
# multiplying each element in l by its count in r,
# and computing the sum
sim_score = sum([(i * Counter(r).get(i, 0)) for i in l])

print(sim_score)
