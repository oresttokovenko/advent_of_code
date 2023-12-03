with open("input.txt", "r") as f:
    input = [line.strip() for line in f]

total = 0

for line in input:
    forwards = line
    backwards = line[::-1]
    for letter in forwards:
        if letter.isnumeric():
            first_letter = letter
            break
    for letter in backwards:
        if letter.isnumeric():
            second_letter = letter
            break
    two_digit_num = first_letter + second_letter
    total += int(two_digit_num)

print(total)
