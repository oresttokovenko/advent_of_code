from dataclasses import dataclass
import math

with open("input.txt", "r") as f:
    input = [i.strip("\n") for i in f.readlines()]
    times = input[0].split()[1:]
    distances = input[1].split()[1:]


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


races = [
    Race(time=int(time), distance=int(distance))
    for time, distance in zip(times, distances)
]

records = []

for i in races:
    num_ways = 0
    results = calc_dist(i.time)
    for k, v in results.items():
        if v > i.distance:
            num_ways += 1
    records.append(num_ways)

print(math.prod(records))
