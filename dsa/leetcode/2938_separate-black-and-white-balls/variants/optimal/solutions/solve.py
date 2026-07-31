def solve(s: str) -> int:
    black_to_left = 0
    steps = 0

    for ball in s:
        if ball == "1":
            black_to_left += 1
        else:
            steps += black_to_left

    return steps
