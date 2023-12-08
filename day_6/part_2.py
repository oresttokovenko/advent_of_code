from dataclasses import dataclass
import re

with open("input.txt", "r") as f:
    input = [i.strip("\n") for i in f.readlines()]

    time = input[0].split(":")[1:]
    time = re.sub(r"\s+", "", "".join(time))

    distance = input[1].split(":")[1:]
    distance = re.sub(r"\s+", "", "".join(distance))


@dataclass
class Race:
    time: int
    distance: int


def calc_dist(time):
    outcomes = {}
    for i in range(time + 1):
        hold = i
        travel = hold * (time - hold)
        outcomes[i] = travel
    return outcomes


only_one_race = Race(time=int(time), distance=int(distance))

num_ways = 0

results = calc_dist(only_one_race.time)
for k, v in results.items():
    if v > only_one_race.distance:
        num_ways += 1

print(num_ways)
