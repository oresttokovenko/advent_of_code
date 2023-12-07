from dataclasses import dataclass
    
@dataclass
class Race:
    time: int
    distance: int
    
with open("example.txt", "r") as f:
    input = [i.strip('\n') for i in f.readlines()]
    times = input[0].split()[1:]
    distances = input[1].split()[1:] 
    
races = [Race(time=int(time), distance=int(distance)) for time, distance in zip(times, distances)]

# wip