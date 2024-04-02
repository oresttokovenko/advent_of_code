with open("input.txt", "r") as f:
    input = [line.strip() for line in f]

matches_list = []

for index, line in enumerate(input):
    # creating two lists from each line
    winning_nums, nums = line[line.find(":") + 1 :].split("|")
    winning_nums = winning_nums.split()
    nums = nums.split()

    # calculating intersection of two sets
    winning_nums = set(map(int, winning_nums))
    nums = set(map(int, nums))
    matches = len(nums & winning_nums)
    matches_list.append(matches)

copies = [1] * len(matches_list)

for i, j in enumerate(matches_list):
    for n in range(i + 1, i + j + 1):
        copies[n] += copies[i]

total = sum(copies)
print(total)
