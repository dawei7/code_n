def solve(s: str) -> int:
    if all(s[index - 1] <= s[index] for index in range(1, len(s))):
        return 0

    minimum = min(s)
    maximum = max(s)
    if s[0] == minimum or s[-1] == maximum:
        return 1

    if len(s) == 2:
        return -1

    if s.find(minimum) == len(s) - 1 and s.rfind(maximum) == 0:
        return 3

    return 2
