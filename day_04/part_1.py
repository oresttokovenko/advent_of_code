with open("input.txt", "r") as f:
    input = [line.strip() for line in f]

points = 0

for line in input:
    # creating two lists from each line
    winning_nums, nums = line[line.find(":") + 1 :].split("|")
    winning_nums = winning_nums.split()
    nums = nums.split()

    # calculating intersection of two sets
    winning_nums = set(map(int, winning_nums))
    nums = set(map(int, nums))
    matches = len(nums & winning_nums)

    # calcluating points using exponents
    points += int(2 ** (matches - 1))

print(points)
