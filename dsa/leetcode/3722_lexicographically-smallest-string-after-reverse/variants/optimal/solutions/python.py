def solve(s: str) -> str:
    smallest = s

    for length in range(2, len(s) + 1):
        smallest = min(smallest, s[:length][::-1] + s[length:])
        smallest = min(smallest, s[:-length] + s[-length:][::-1])

    return smallest
