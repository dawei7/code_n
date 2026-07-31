"""App-local reference solution for LeetCode 2833."""


def solve(moves: str) -> int:
    """Return the greatest possible final distance from the origin."""
    displacement = 0
    flexible = 0

    for move in moves:
        if move == "L":
            displacement -= 1
        elif move == "R":
            displacement += 1
        else:
            flexible += 1

    return abs(displacement) + flexible
