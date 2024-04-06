# part 1

from pathlib import Path

p = Path("input.txt").read_text().rstrip("\n").split("\n")
p = [tuple(map(lambda x: int(x), i.split("x"))) for i in p]

# l * w * h
# 2*l*w + 2*w*h + 2*h*l

type PresentType = list[tuple[int, ...]]


def calc_square_foot(l: int, w: int, h: int) -> int:
    return 2 * (l * w) + 2 * (w * h) + 2 * (h * l) + min(l * w, w * h, h * l)


def wrapping_paper(presents: PresentType) -> int:
    total_square_feet = 0
    for l, w, h in presents:
        present_dimenions = calc_square_foot(l, w, h)
        total_square_feet += present_dimenions
    return total_square_feet


if __name__ == "__main__":
    result = wrapping_paper(p)
    print(result)
