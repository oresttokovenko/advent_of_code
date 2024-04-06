# part 2

import heapq
from pathlib import Path

p = Path("input.txt").read_text().rstrip("\n").split("\n")
p = [tuple(map(lambda x: int(x), i.split("x"))) for i in p]

type PresentType = list[tuple[int, ...]]


def calc_ribbon_len(l: int, w: int, h: int) -> tuple[int, int]:
    two_shortest = heapq.nsmallest(2, (l, w, h))
    ribbon = two_shortest[0] + two_shortest[0] + two_shortest[1] + two_shortest[1]
    bow = l * w * h
    return ribbon, bow


def wrapping_ribbon(presents: PresentType) -> int:
    feet_of_ribbon = 0
    for l, w, h in presents:
        ribbon, bow = calc_ribbon_len(l, w, h)
        feet_of_ribbon += ribbon + bow
    return feet_of_ribbon


if __name__ == "__main__":
    result = wrapping_ribbon(p)
    print(result)
