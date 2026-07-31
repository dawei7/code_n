def solve(current: str, correct: str) -> int:
    def minutes(time: str) -> int:
        return int(time[:2]) * 60 + int(time[3:])

    remaining = minutes(correct) - minutes(current)
    operations = 0
    for increment in (60, 15, 5, 1):
        count, remaining = divmod(remaining, increment)
        operations += count
    return operations
