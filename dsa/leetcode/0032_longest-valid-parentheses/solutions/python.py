def solve(s: str) -> int:
    best = opened = closed = 0
    for char in s:
        opened += char == "("
        closed += char == ")"
        if opened == closed:
            best = max(best, 2 * closed)
        elif closed > opened:
            opened = closed = 0

    opened = closed = 0
    for char in reversed(s):
        opened += char == "("
        closed += char == ")"
        if opened == closed:
            best = max(best, 2 * opened)
        elif opened > closed:
            opened = closed = 0
    return best
