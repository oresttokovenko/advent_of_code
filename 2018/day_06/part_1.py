# part 1
# wip

from pathlib import Path
from itertools import repeat
from typing import Literal

type Grid = list[list[int]]

p = Path("input.txt").read_text().rstrip('\n').split('\n')
p = [tuple(map(lambda x: int(x), i.split(', '))) for i in p]

# grid size doesn't really matter, picking arbitrary 
def generate_grid(n: Literal[400]) -> Grid:
    return [['.' for _ in range(n)] for _ in range(n)]

# infinite means touching edge
def place_coordinates(grid: Grid, coordinates: list[tuple]) -> Grid:
    for idx, (i,j) in enumerate(coordinates):
        grid[i][j] == idx + 1
    return grid


if __name__ == "__main__":
    grid = generate_grid(400)
    updated_grid = place_coordinates(grid, p)
    ...