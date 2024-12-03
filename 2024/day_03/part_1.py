import re
from operator import mul
from pathlib import Path

p = Path("input.txt").read_text()

if __name__ == "__main__":
    # fetching all instances of `mul(<num>,<num>)`
    pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
    matches = re.findall(pattern, p)
    result = sum(mul(int(i[0]), int(i[1])) for i in matches)
    print(result)
