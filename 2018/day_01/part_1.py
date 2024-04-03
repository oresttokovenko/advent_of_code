# part 1

from collections.abc import Sequence
from pathlib import Path

p = Path.open("input.txt").readlines()  # type: ignore
p = [int(i.strip("\n")) for i in p]


def frequency_change(input: Sequence) -> int:
    p_sum = sum(input)
    return p_sum


if __name__ == "__main__":
    result = frequency_change(p)
    print(result)
