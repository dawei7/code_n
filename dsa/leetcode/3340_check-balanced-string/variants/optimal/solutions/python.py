def solve(num: str) -> bool:
    difference = 0

    for index, digit in enumerate(num):
        value = ord(digit) - ord("0")
        if index % 2 == 0:
            difference += value
        else:
            difference -= value

    return difference == 0
