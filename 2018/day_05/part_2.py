# part 2

from pathlib import Path
from string import ascii_lowercase, ascii_uppercase
from typing import TypedDict
from itertools import groupby

p = Path("input.txt").read_text().strip()

def generate_unit_combinations() -> set:
    upper_lower = list(
        map(lambda x: x[0] + x[1], zip(ascii_uppercase, ascii_lowercase, strict=False))
    )
    return upper_lower + list(map(lambda x: "".join(reversed(x)), upper_lower))

def grouping_units(units: set) -> set:
    sorted_units = sorted(units, key=lambda x: x[0].lower())
    return set([tuple(i) for _, i in groupby(sorted_units, key=lambda x: x[0].lower())])

def reacting(polymer: str, units: list[tuple]) -> str:
    shortest_polymer = []
    replaced = True
    while replaced:
        for i in units:
            for j in i:
                new_polymer = polymer.replace(j, "")
                if polymer != new_polymer:
                    shortest_polymer.append(len(new_polymer))
                    replaced = True
        print(shortest_polymer)
        return min(shortest_polymer)


if __name__ == "__main__":
    units = generate_unit_combinations()
    grouped_units = grouping_units(units)
    result = reacting(p, grouped_units)
    print(result)
