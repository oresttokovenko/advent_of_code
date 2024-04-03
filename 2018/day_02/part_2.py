# part 2

from collections.abc import Sequence
from difflib import ndiff
from itertools import combinations
from operator import contains
from pathlib import Path

p = Path.open("input.txt").readlines()  # type: ignore
p = [i.strip("\n") for i in p]


def correct_box_id(input: Sequence) -> tuple:
    candidates = tuple()
    for i in combinations([i for i in input], 2):
        delta = ndiff(i[0], i[1])
        diff_letter = [
            i.strip() for i in delta if not contains(i, "-") and not contains(i, "+")
        ]
        # returning tuple pair which differ by exactly one character
        if len(diff_letter) == len(i[0]) - 1:
            candidates = (i[0], i[1])
    return candidates


def common_letters(candidate: tuple) -> str:
    string1, string2 = candidate[0], candidate[1]
    # returning only matching letters by index, ordered
    chars = [(idx, i) for idx, i in enumerate(string1) if string1[idx] == string2[idx]]
    # unpacking list of tuples
    _, matching_letters = zip(*chars, strict=False)
    matching_letters = "".join(matching_letters)
    return matching_letters


if __name__ == "__main__":
    boxes = correct_box_id(p)
    result = common_letters(boxes)
    print(result)
