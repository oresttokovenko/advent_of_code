# part 1

from collections import defaultdict
from pathlib import Path

p = Path("input.txt").read_text().split("\n")


def parse_time(line: str) -> str:
    words = line.split()
    _, time = words[0][1:], words[1][:-1]
    return int(time.split(":")[1])


def guard_duty_parse(schedule: list[str]) -> defaultdict[int]:
    asleep_at_each_minute = defaultdict(int)
    guard = None
    asleep = None
    for line in schedule:
        if line:
            time = parse_time(line)
            if "begins shift" in line:
                guard = int(line.split()[3][1:])
                asleep = None
            elif "falls asleep" in line:
                asleep = time
            elif "wakes up" in line:
                for t in range(asleep, time):
                    asleep_at_each_minute[(guard, t)] += 1
    return asleep_at_each_minute


def maximum(schedule_parsed: defaultdict):
    key = max(schedule_parsed, key=schedule_parsed.get)
    return key, schedule_parsed[key]


if __name__ == "__main__":
    p.sort()
    guard_duty_parsed = guard_duty_parse(p)
    best_guard, best_min = maximum(guard_duty_parsed)
    result = best_guard * best_min
    print(result)
