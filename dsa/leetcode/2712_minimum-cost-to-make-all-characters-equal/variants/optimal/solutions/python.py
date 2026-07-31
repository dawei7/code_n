def solve(s: str) -> int:
    length = len(s)
    cost = 0

    for index in range(1, length):
        if s[index] != s[index - 1]:
            cost += min(index, length - index)

    return cost

