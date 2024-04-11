# part 1

from collections.abc import Sequence
from pathlib import Path

p = Path("input.txt").read_text().split("\n")


def calibration_values(values: Sequence) -> int:
    total = 0
    for value in values:
        nums = [i for i in value if i.isnumeric()]
        two_digit = int(nums[0] + nums[-1])
        total += two_digit

    return total


if __name__ == "__main__":
    result = calibration_values(p)
    print(result)
