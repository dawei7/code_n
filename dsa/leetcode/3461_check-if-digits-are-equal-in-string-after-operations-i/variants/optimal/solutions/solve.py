def solve(s: str) -> bool:
    steps = len(s) - 2
    coefficient = 1
    difference = 0

    for index in range(steps + 1):
        difference = (difference + coefficient * (ord(s[index]) - ord(s[index + 1]))) % 10
        if index < steps:
            coefficient = coefficient * (steps - index) // (index + 1)

    return difference == 0
