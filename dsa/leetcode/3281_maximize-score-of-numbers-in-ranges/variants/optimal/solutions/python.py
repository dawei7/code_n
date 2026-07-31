def solve(start: list[int], d: int) -> int:
    ordered = sorted(start)

    def feasible(distance: int) -> bool:
        previous = ordered[0]
        for interval_start in ordered[1:]:
            chosen = max(interval_start, previous + distance)
            if chosen > interval_start + d:
                return False
            previous = chosen
        return True

    low = 0
    high = (ordered[-1] + d - ordered[0]) // (len(ordered) - 1)
    answer = 0

    while low <= high:
        middle = (low + high) // 2
        if feasible(middle):
            answer = middle
            low = middle + 1
        else:
            high = middle - 1

    return answer
