def solve(start: list[int], target: list[int]) -> bool:
    return (start[0] + start[1]) % 2 == (target[0] + target[1]) % 2
