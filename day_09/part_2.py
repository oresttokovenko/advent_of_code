with open("input.txt", "r") as f:
    input = [[int(j) for j in i.strip().split()] for i in f]


# recursively extrapolating the next value, backwards
def extrapolate(sequence):
    nums = []
    for i in range(len(sequence) - 1):
        nums.append(sequence[i + 1] - sequence[i])
    if all(j == 0 for j in nums):
        return sequence[0]
    else:
        return sequence[0] + -1 * extrapolate(nums)


all_values = 0

for line in input:
    all_values += extrapolate(line)

print(all_values)
