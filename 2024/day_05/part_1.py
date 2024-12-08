from collections.abc import Sequence
from pathlib import Path
from typing import NamedTuple

p = Path("input.txt").read_text().split("\n")
p = p[:-1] if p and p[-1] == "" else p


class Rule(NamedTuple):
    before: int
    after: int


def validate_page_order(page_numbers: list[int], rules: list[Rule]) -> bool:
    """returns False if a rule fails, otherwise True if all rules are satisfied"""
    i = 0
    while i < len(rules):
        rule = rules[i]
        if (
            rule.before in page_numbers
            and rule.after in page_numbers
            and page_numbers.index(rule.before) > page_numbers.index(rule.after)
        ):
            return False
        i += 1
    return True


def get_middle_value(array: Sequence) -> int:
    """returns the value at the middle most index of an odd len array"""
    middle_index = len(array) // 2
    return array[middle_index]


if __name__ == "__main__":
    split_index = p.index("")
    rules = [Rule(*map(int, rule.split("|"))) for rule in p[:split_index]]
    numbers = [list(map(int, rule.split(","))) for rule in p[split_index + 1 :]]

    result = sum(get_middle_value(update) for update in numbers if validate_page_order(update, rules))
    print(result)
