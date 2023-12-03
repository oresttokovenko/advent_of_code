with open("input.txt", "r") as f:
    input = [line.lstrip("Game ") for line in f]

parsed_games = {}
cube_powers = 0

# creating a dictionary with the game number as the key, and a list of lists as the value
for game in input:
    game_number, game_data = game.split(":", 1)
    parts = [part.strip() for part in game_data.split(";")]
    colour_counts = [
        [colour_count.strip() for colour_count in part.split(",")] for part in parts
    ]
    parsed_games[int(game_number)] = colour_counts

# iterating through the sub list iterables, appending the minimum number to the game level dict value
for game_number, line in parsed_games.items():
    fewest_counts = {"red": 0, "green": 0, "blue": 0}
    for sub_line in line:
        for cube in sub_line:
            cube_count, cube_colour = cube.split(" ")
            cube_count = int(cube_count)
            if cube_colour in fewest_counts and cube_count > fewest_counts[cube_colour]:
                fewest_counts[cube_colour] = cube_count
    power = fewest_counts["red"] * fewest_counts["green"] * fewest_counts["blue"]
    cube_powers += power

print(cube_powers)
