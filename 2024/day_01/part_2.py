from collections import Counter
from itertools import islice
from pathlib import Path

p = Path("input.txt").read_text().split()


def split_list(input: list[str], start_iter: int) -> list[int]:
    """splitting into two lists"""
    return [int(i) for i in islice(input, start_iter, None, 2)]


if __name__ == "__main__":
    l = split_list(p, 0)
    r = split_list(p, 1)
    # counting occurrences of elements in r
    # multiplying each element in l by its count in r,
    # and computing the sum
    result = sum([(i * Counter(r).get(i, 0)) for i in l])
    print(result)
