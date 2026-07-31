def solve(side: int, points: list[list[int]], k: int) -> int:
    perimeter = 4 * side
    positions = []

    for x, y in points:
        if y == 0:
            positions.append(x)
        elif x == side:
            positions.append(side + y)
        elif y == side:
            positions.append(3 * side - x)
        else:
            positions.append(4 * side - y)

    positions.sort()
    count = len(positions)
    extended = positions + [position + perimeter for position in positions]
    doubled_count = 2 * count
    levels = (k - 1).bit_length()

    def can_place(minimum: int) -> bool:
        next_index = [doubled_count] * (doubled_count + 1)
        right = 1

        for left in range(doubled_count):
            if right <= left:
                right = left + 1
            target = extended[left] + minimum
            while right < doubled_count and extended[right] < target:
                right += 1
            next_index[left] = right

        jumps = [next_index]
        for _ in range(1, levels):
            previous = jumps[-1]
            jumps.append([previous[previous[index]] for index in range(doubled_count + 1)])

        for start in range(count):
            current = start
            remaining = k - 1
            bit = 0
            while remaining:
                if remaining & 1:
                    current = jumps[bit][current]
                remaining >>= 1
                bit += 1

            if current < doubled_count and extended[current] <= positions[start] + perimeter - minimum:
                return True

        return False

    low = 1
    high = side
    while low < high:
        middle = (low + high + 1) // 2
        if can_place(middle):
            low = middle
        else:
            high = middle - 1

    return low
