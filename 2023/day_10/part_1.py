# with open("input.txt", "r") as f:
#     input = [i.split() for i in f]

from pathlib import Path

input_path = Path("input.txt")
input = input_path.read_text()

print(input)