with open("input", "r") as f:
    input = [line.strip() for line in f]

total = 0

valid_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

valid_digits_reversed = {i[::-1]: j for i, j in valid_digits.items()}

for line in input:
    spelled_out_fwd = ""
    spelled_out_bck = ""

    forwards = line
    backwards = line[::-1]

    for letter in forwards:
        found = False
        if letter.isnumeric():
            first_letter = letter
            break
        else:
            spelled_out_fwd += letter
            for key in valid_digits.keys():
                if key in spelled_out_fwd:
                    first_letter = valid_digits[key]
                    found = True
                    break
            if found:
                break
    for letter in backwards:
        found = False
        if letter.isnumeric():
            second_letter = letter
            break
        else:
            spelled_out_bck += letter
            for key in valid_digits_reversed.keys():
                if key in spelled_out_bck:
                    second_letter = valid_digits_reversed[key]
                    found = True
                    break
            if found:
                break
    two_digit_num = first_letter + second_letter
    total += int(two_digit_num)

print(total)
