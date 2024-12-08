from collections.abc import Sequence
from pathlib import Path
from typing import NamedTuple

p = Path("input.txt").read_text().split("\n")
p = p[:-1] if p and p[-1] == "" else p


class Rule(NamedTuple):
    before: int
    after: int


def is_rule_violated(page_numbers: list[int], rule: Rule) -> bool:
    """Checks if a specific rule is violated"""
    if rule.before in page_numbers and rule.after in page_numbers:
        return page_numbers.index(rule.before) > page_numbers.index(rule.after)
    return False


def is_update_incorrect(page_numbers: list[int], rules: list[Rule]) -> bool:
    """Returns True if any rule in an update is violated otherwise False"""
    for rule in rules:
        if is_rule_violated(page_numbers, rule):
            return True
    return False


def fix_update(page_numbers: list[int], rules: list[Rule]) -> list[int]:
    """Corrects page order based on rules"""
    i = 0
    while i < len(rules):
        rule = rules[i]
        if is_rule_violated(page_numbers, rule):
            b = page_numbers.index(rule.before)
            a = page_numbers.index(rule.after)
            page_numbers[b], page_numbers[a] = page_numbers[a], page_numbers[b]
        i += 1
    return page_numbers


def get_middle_value(array: Sequence) -> int:
    """returns the value at the middle most index of an odd length array"""
    middle_index = len(array) // 2
    return array[middle_index]


if __name__ == "__main__":
    split_index = p.index("")
    rules = [Rule(*map(int, rule.split("|"))) for rule in p[:split_index]]
    numbers = [list(map(int, rule.split(","))) for rule in p[split_index + 1 :]]

    correct_orderings = []
    for update in numbers:
        if is_update_incorrect(update, rules):
            correct_orderings.append(fix_update(update, rules))

    result = sum(get_middle_value(update) for update in correct_orderings)
    print(result)
