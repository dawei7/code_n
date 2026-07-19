def solve(s: str, p: str) -> bool:
    previous = [False] * (len(p) + 1)
    previous[0] = True
    for index, token in enumerate(p, start=1):
        previous[index] = token == "*" and previous[index - 1]

    for char in s:
        current = [False] * (len(p) + 1)
        for index, token in enumerate(p, start=1):
            if token == "*":
                current[index] = current[index - 1] or previous[index]
            else:
                current[index] = previous[index - 1] and (token == "?" or token == char)
        previous = current
    return previous[-1]
