from pathlib import Path

p = Path("input.txt").read_text().splitlines()
p = [tuple(map(lambda x: int(x), i.split())) for i in p]

def is_report_safe(report: tuple[int]) -> bool:
    """
    This function returns true if:
    The levels are either all increasing or all decreasing
    Any two adjacent levels differ by at least one and at most three
    """
    consecutive_diff = [t - s for s, t in zip(report, report[1:], strict=False)]
    return (
        all(x in {1, 2, 3} for x in consecutive_diff) or
        all(x in {-1, -2, -3} for x in consecutive_diff)
    )


if __name__ == "__main__":
    result = sum(1 for i in p if is_report_safe(i))
    print(result)