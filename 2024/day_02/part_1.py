from pathlib import Path

p = Path("input.txt").read_text().splitlines()
p = [tuple(map(lambda x: int(x), i.split())) for i in p]


def calc_diff(report: tuple[int]) -> list[int]:
    """calculating the consecutive differences in the report"""
    return [curr - prev for curr, prev in zip(report, report[1:], strict=False)]


def is_report_safe(report: tuple[int]) -> bool:
    """
    this function returns true if:
    - the levels are either all increasing or all decreasing
    - any two adjacent levels differ by at least one and at most three
    """
    diff = calc_diff(report)
    return all(x in {1, 2, 3} for x in diff) or all(x in {-1, -2, -3} for x in diff)


if __name__ == "__main__":
    result = sum(1 for i in p if is_report_safe(i))
    print(result)
