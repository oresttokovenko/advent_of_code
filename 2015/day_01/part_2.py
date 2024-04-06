# part 2

from collections.abc import Sequence
from pathlib import Path

p = Path("input.txt").read_text().strip()


def get_basement_position(instructions: Sequence) -> int:
    position = 0
    for idx, i in enumerate(instructions):
        match i:
            case "(":
                position += 1
            case ")":
                position -= 1
        if position == -1:
            return idx + 1


if __name__ == "__main__":
    result = get_basement_position(p)
    print(result)
