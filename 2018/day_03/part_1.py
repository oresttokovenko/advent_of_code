# part 1

import re
from collections import Counter
from itertools import chain, product, repeat
from pathlib import Path
from typing import Literal

type Grid = list[list]
type Claim = tuple[int, int, int, int]

p = Path.open("input.txt").readlines()  # type: ignore
# removing claim number
p = [i.strip("\n").split("@")[1] for i in p]
# extracting numerical substrings
p = [re.findall(r"\d+", i) for i in p]
# casting elements in each sublist to an int and converting to tuple
p = [tuple(map(lambda x: int(x), i)) for i in p]


def generate_grid(n: Literal[1000]) -> Grid:
    return [list(repeat(0, n)) for i in range(n)]


def place_claim(grid: Grid, claims: list[Claim]) -> Grid:
    for left_edge, top_edge, width, height in claims:
        top_left_corner, bottom_right_corner = (
            (left_edge, top_edge),
            (left_edge + width, top_edge + height),
        )
        # creating a product from every coordinate around the perimeter of the claim, then updating the grid
        for row, col in product(
            range(top_left_corner[0], bottom_right_corner[0]),
            range(top_left_corner[1], bottom_right_corner[1]),
        ):
            # overlapping claims are marked with an 'x'
            grid[row][col] = "x" if grid[row][col] != 0 else 1
    return grid


def count_overlap(grid: Grid) -> int:
    flat_grid = tuple(chain.from_iterable(grid))
    overlap_count = Counter(flat_grid)
    return overlap_count["x"]


if __name__ == "__main__":
    fabric = generate_grid(1000)
    assert len(fabric) == 1000, "y axis must be 1000 units"
    assert len(fabric[0]) == 1000, "x axis must be 1000 units"
    claimed_fabric = place_claim(fabric, p)
    result = count_overlap(claimed_fabric)
    print(result)
