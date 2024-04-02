with open("example.txt", "r") as f:
    input = [line.strip() for line in f]
    _, seeds = input[0].split(":")
    seeds = [int(seed) for seed in seeds.split()]
    maps = input[2:]

result_dict = {}

# keeping track of current key
current_key = None

for line in maps:
    if line:
        # checking if the line is a map title
        if "map:" in line:
            # extracting the key from the title
            current_key = line.replace(" map:", "")
            result_dict[current_key] = []
        else:
            # processing the line as a list of integers and add it to the current key
            numbers = list(map(int, line.split()))
            result_dict[current_key].append(numbers)

# temp
# temp = result_dict["seed-to-soil"]

map_dict = {}

for i in range(len(temp)):
    dest_range_num = temp[i][0]
    source_range_num = temp[i][1]
    range_len_num = temp[i][2]
    dest_range = [i for i in range(dest_range_num, dest_range_num + range_len_num)]
    source_range = [
        i for i in range(source_range_num, source_range_num + range_len_num)
    ]

# wip