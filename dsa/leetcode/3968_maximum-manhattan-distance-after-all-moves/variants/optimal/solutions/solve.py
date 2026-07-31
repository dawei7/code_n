def solve(moves: str) -> int:
    horizontal = 0
    vertical = 0
    wildcards = 0

    for move in moves:
        if move == "U":
            vertical += 1
        elif move == "D":
            vertical -= 1
        elif move == "L":
            horizontal -= 1
        elif move == "R":
            horizontal += 1
        else:
            wildcards += 1

    return abs(horizontal) + abs(vertical) + wildcards
