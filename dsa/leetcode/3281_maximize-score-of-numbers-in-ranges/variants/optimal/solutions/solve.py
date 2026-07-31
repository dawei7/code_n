def solve(start: list[int], d: int) -> int:
    start.sort()

    def feasible(distance: int) -> bool:
        previous = start[0]
        for interval_start in start[1:]:
            chosen = max(interval_start, previous + distance)
            if chosen > interval_start + d:
                return False
            previous = chosen
        return True

    low = 0
    high = (start[-1] + d - start[0]) // (len(start) - 1)
    answer = 0

    while low <= high:
        middle = (low + high) // 2
        if feasible(middle):
            answer = middle
            low = middle + 1
        else:
            high = middle - 1

    return answer
