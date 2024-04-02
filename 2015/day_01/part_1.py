# part 1
from collections import Counter
from collections.abc import Sequence
from pathlib import Path

p = Path.open('input.txt').readline() # type: ignore


def deliver_presents(input: Sequence) -> int:
    c = Counter(input)
    return c['('] - c[')']

if __name__ == "__main__":
    result = deliver_presents(p)
    print(result)