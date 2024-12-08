from dataclasses import dataclass
from pathlib import Path

p = Path("input.txt").read_text().split("\n")


@dataclass
class Equation:
    value: int
    test_values: list[int]


def calculate(nums: list[int]) -> list[int]:
    """rescursively getting all combinations"""
    if len(nums) == 1:
        return nums
    return (calculate([nums[0] + nums[1]] + nums[2:]) + calculate([nums[0] * nums[1]] + nums[2:])) + calculate(
        [int(str(nums[0]) + str(nums[1]))] + nums[2:]
    )


if __name__ == "__main__":
    equations = []
    result = 0
    for line in p:
        try:
            value, test_values = line.split(": ")
        except ValueError:
            pass
        equations.append(Equation(value=int(value), test_values=[int(val) for val in test_values.split()]))

    for line in equations:
        value = line.value
        results = calculate(line.test_values)

        if value in results:
            result += value

    print(result)
