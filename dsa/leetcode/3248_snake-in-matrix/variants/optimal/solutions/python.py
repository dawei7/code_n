def solve(n: int, commands: list[str]) -> int:
    movement = {
        "UP": -n,
        "RIGHT": 1,
        "DOWN": n,
        "LEFT": -1,
    }
    return sum(movement[command] for command in commands)
