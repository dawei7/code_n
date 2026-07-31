def solve(s: str, t: str) -> int:
    source = 0
    target = 0
    removed = False

    while source < len(s) and target < len(t):
        if s[source] == t[target]:
            source += 1
            target += 1
        elif not removed:
            removed = True
            source += 1
        else:
            break

    return target
