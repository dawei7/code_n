def solve(n: int, x: int, y: int) -> list[int]:
    if x > y:
        x, y = y, x

    if y - x <= 1:
        return [2 * (n - distance) for distance in range(1, n + 1)]

    left_length = x - 1
    right_length = n - y
    cycle_length = y - x + 1
    unordered = [0] * (n + 1)
    difference = [0] * (n + 2)

    def add_range(start: int, end: int, value: int) -> None:
        if start <= end:
            difference[start] += value
            difference[end + 1] -= value

    for distance in range(1, left_length + 1):
        unordered[distance] += left_length + 1 - distance
    for distance in range(1, right_length + 1):
        unordered[distance] += right_length + 1 - distance

    for distance in range(1, (cycle_length - 1) // 2 + 1):
        unordered[distance] += cycle_length
    if cycle_length % 2 == 0:
        unordered[cycle_length // 2] += cycle_length // 2

    for cycle_distance in range(1, cycle_length // 2 + 1):
        multiplicity = (
            1
            if cycle_length % 2 == 0 and cycle_distance == cycle_length // 2
            else 2
        )
        add_range(cycle_distance + 1, cycle_distance + left_length, multiplicity)
        add_range(cycle_distance + 1, cycle_distance + right_length, multiplicity)

    for left_distance in range(1, left_length + 1):
        add_range(left_distance + 2, left_distance + right_length + 1, 1)

    running = 0
    answer = [0] * n
    for distance in range(1, n + 1):
        running += difference[distance]
        unordered[distance] += running
        answer[distance - 1] = 2 * unordered[distance]

    return answer
