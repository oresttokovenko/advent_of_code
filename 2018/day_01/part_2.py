# part 2

from collections import defaultdict
from collections.abc import Sequence
from itertools import accumulate
from pathlib import Path

p = Path.open("input.txt").readlines()  # type: ignore
p = [int(i.strip("\n")) for i in p]


def frequency_change(input: Sequence) -> int:
    d = defaultdict(int)
    # returning array of accumulated sum
    frequencies = accumulate(input)
    for i in frequencies:
        d[i] += 1
        if d[i] == 2:
            return d[i]
    return -1


if __name__ == "__main__":
    result = frequency_change(p)
    print(result)
