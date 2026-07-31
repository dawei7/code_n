def solve(s: str) -> int:
    ones = 0
    operations = 0
    for index, character in enumerate(s):
        if character == "1":
            ones += 1
        elif index > 0 and s[index - 1] == "1":
            operations += ones
    return operations
