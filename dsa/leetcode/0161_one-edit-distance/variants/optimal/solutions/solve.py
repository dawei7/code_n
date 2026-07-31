def solve(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
        return False
    if len(s) > len(t):
        s, t = t, s

    first = 0
    second = 0
    edits = 0
    while first < len(s) and second < len(t):
        if s[first] == t[second]:
            first += 1
            second += 1
            continue
        edits += 1
        if edits > 1:
            return False
        if len(s) == len(t):
            first += 1
        second += 1

    if second < len(t):
        edits += 1
    return edits == 1
