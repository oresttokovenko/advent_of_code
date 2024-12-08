from itertools import product
from pathlib import Path

p = Path("input.txt").read_text().split('\n')

def check_neighbours(coordinate: tuple[int, int], directions: list[tuple[int, int]]) -> list[tuple[int,int]]:
    return [[x + coordinate[0], y + coordinate[1]] for x, y in directions]

if __name__ == "__main__":
    result = 0
    possible_words = []
    directions = [i for i in product((3, -3, 0), repeat=2) if i != (0,0)]
    rows = len(p)
    cols = len(p[0])

    for row in range(rows):
        for col in range(cols):
            if p[row][col] == 'X':
                neighbours = check_neighbours((row, col), directions)
                for i, j in neighbours:
                    # accessing the neighbour via coordinates
                    try:
                        word = ''.join(
                            p[x][y]
                            for x, y in zip(
                                range(row, i + 1 if i > row else i - 1, 1 if i > row else -1),
                                range(col, j + 1 if j > col else j - 1, 1 if j > col else -1), strict=False
                            )
                        )
                        if word:
                            possible_words.append(word)
                            print(word)
                    except IndexError:
                        pass
    result += sum(1 for i in possible_words if 'XMAS' in i)
    print(result)

