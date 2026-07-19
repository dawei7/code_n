def solve(ranges: list[list[int]], left: int, right: int) -> bool:
    difference = [0] * 52
    for start, end in ranges:
        difference[start] += 1
        difference[end + 1] -= 1

    active = 0
    for value in range(1, right + 1):
        active += difference[value]
        if value >= left and active == 0:
            return False

    return True
