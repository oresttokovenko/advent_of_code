with open("input.txt", "r") as f:
    input = [line.lstrip("Game ") for line in f]

parsed_games = {}
impossible_games = []
bag = {"red": 12, "green": 13, "blue": 14}

# creating a dictionary with the game number as the key, and a list of lists as the value
for game in input:
    game_number, game_data = game.split(":", 1)
    parts = [part.strip() for part in game_data.split(";")]
    colour_counts = [
        [colour_count.strip() for colour_count in part.split(",")] for part in parts
    ]
    parsed_games[int(game_number)] = colour_counts

# iterating through the sub list iterables, checking if the count of cubes is less than the max in the bag
for game_number, line in parsed_games.items():
    for sub_line in line:
        for cube in sub_line:
            cube_count, cube_colour = cube.split(" ")
            if cube_colour in bag.keys() and int(cube_count) > bag[cube_colour]:
                impossible_games.append(game_number)

# fetching list of possible games by filtering out impossible games
result = sum([game for game in parsed_games.keys() if game not in impossible_games])
print(result)
