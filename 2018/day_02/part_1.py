# part 1

from collections import Counter
from collections.abc import Sequence
from pathlib import Path
from typing import Literal

p = Path.open("input.txt").readlines()  # type: ignore
p = [i.strip("\n") for i in p]


def warehouse_search(input: Sequence, num_letters: Literal[2, 3]):
    multiples = 0
    for i in input:
        counter = Counter(i)
        values = set(counter.values())
        if num_letters in values:
            multiples += 1
    return multiples


if __name__ == "__main__":
    exactly_two = warehouse_search(p, 2)
    exactly_three = warehouse_search(p, 3)
    result = exactly_two * exactly_three
    print(result)
