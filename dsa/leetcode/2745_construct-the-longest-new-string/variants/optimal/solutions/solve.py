def solve(x: int, y: int, z: int) -> int:
    blocks = 2 * min(x, y) + z
    if x != y:
        blocks += 1
    return 2 * blocks
