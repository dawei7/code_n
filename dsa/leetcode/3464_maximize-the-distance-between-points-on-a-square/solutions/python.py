def solve(side: int, points: list[list[int]], k: int) -> int:
    def perimeter_position(x: int, y: int) -> int:
        if y == 0:
            return x
        if x == side:
            return side + y
        if y == side:
            return 3 * side - x
        return 4 * side - y

    perimeter = 4 * side
    positions = sorted(perimeter_position(x, y) for x, y in points)
    n = len(positions)
    doubled = positions + [position + perimeter for position in positions]

    def feasible(distance: int) -> bool:
        next_index = [0] * (2 * n)
        pointer = 0
        for index in range(2 * n):
            if pointer < index + 1:
                pointer = index + 1
            while pointer < 2 * n and doubled[pointer] - doubled[index] < distance:
                pointer += 1
            next_index[index] = pointer

        for start in range(n):
            current = start
            possible = True
            for _ in range(k - 1):
                current = next_index[current]
                if current >= start + n:
                    possible = False
                    break
            if possible and doubled[current] - doubled[start] <= perimeter - distance:
                return True
        return False

    low, high = 1, perimeter // k
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if feasible(mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return answer
