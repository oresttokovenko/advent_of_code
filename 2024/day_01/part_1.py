from itertools import islice
from pathlib import Path

p = Path("input.txt").read_text().split()


def split_and_sort_list(input: list[str], start_iter: int) -> list[int]:
    """splitting into two lists and sorting in ascending order"""
    return sorted([int(i) for i in islice(input, start_iter, None, 2)])


if __name__ == "__main__":
    l = split_and_sort_list(p, 0)
    r = split_and_sort_list(p, 1)
    result = (total_distance := sum(abs(i - j) for i, j in zip(l, r, strict=False)))
    print(result)
