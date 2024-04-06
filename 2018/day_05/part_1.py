# part 1

from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

p = Path("input.txt").read_text().strip()

upper_lower = set(
    map(lambda x: x[0] + x[1], zip(ascii_uppercase, ascii_lowercase, strict=False))
)
units = upper_lower | set(map(lambda x: "".join(reversed(x)), upper_lower))


def reacting(polymer: str, units: set[str]) -> str:
    replaced = True
    while replaced:
        replaced = False
        for i in units:
            new_polymer = polymer.replace(i, "")
            if polymer != new_polymer:
                replaced = True
                polymer = new_polymer
    return len(polymer)


if __name__ == "__main__":
    result = reacting(p, units)
    print(result)
