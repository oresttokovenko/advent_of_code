spelled_out_fwd = "zone"

valid_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


for key in valid_digits.keys():
    if key in spelled_out_fwd:
        print(key)