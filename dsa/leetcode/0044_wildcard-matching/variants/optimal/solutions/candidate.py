def solve(s: str, p: str) -> bool:
    previous = [False] * (len(p) + 1)
    previous[0] = True
    for j, token in enumerate(p, start=1):
        previous[j] = token == "*" and previous[j - 1]

    for char in s:
        current = [False] * (len(p) + 1)
        for j, token in enumerate(p, start=1):
            if token == "*":
                current[j] = current[j - 1] or previous[j]
            else:
                current[j] = previous[j - 1] and (token == "?" or token == char)
        previous = current
    return previous[-1]
