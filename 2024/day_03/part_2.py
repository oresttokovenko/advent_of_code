import re
from operator import mul
from pathlib import Path

p = Path("input.txt").read_text()


def enabled_multiplications(corr_instructions: list[str]) -> list[str]:
    """processes a list of instructions appending only enabled instructions"""
    instructions = []
    enabled = True
    for i in corr_instructions:
        if "do()" in i:
            enabled = True
        elif "don't()" in i:
            enabled = False
        elif enabled:
            instructions.append(i)
    return instructions


if __name__ == "__main__":
    # matching `mul(<num>,<num>)`
    mul_pattern = r"mul\(\d{1,3},\s*\d{1,3}\)"
    # matching `do()`
    do_pattern = r"do\(\)"
    # matching `don't()`
    dont_pattern = r"don't\(\)"

    pattern = rf"{mul_pattern}|{dont_pattern}|{do_pattern}"
    corr_instructions = re.findall(pattern, p)

    result = sum(
        mul(int(a), int(b))
        for a, b in (
            match[4:-1].split(",")
            for match in enabled_multiplications(corr_instructions)
        )
    )
    print(result)
