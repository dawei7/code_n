def solve(number: str, digit: str) -> str:
    removal = -1
    for index, value in enumerate(number):
        if value != digit:
            continue
        removal = index
        if index + 1 < len(number) and number[index + 1] > digit:
            break
    return number[:removal] + number[removal + 1 :]
