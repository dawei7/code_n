def solve(s: str) -> bool:
    low = 0
    high = 0
    for character in s:
        if character == "(":
            low += 1
            high += 1
        elif character == ")":
            low -= 1
            high -= 1
        else:
            low -= 1
            high += 1

        if high < 0:
            return False
        low = max(low, 0)

    return low == 0

