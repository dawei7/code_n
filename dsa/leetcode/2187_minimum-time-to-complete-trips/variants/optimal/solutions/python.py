def solve(time: list[int], totalTrips: int) -> int:
    low = 1
    high = min(time) * totalTrips

    while low < high:
        middle = (low + high) // 2
        completed = 0
        for duration in time:
            completed += middle // duration
            if completed >= totalTrips:
                break

        if completed >= totalTrips:
            high = middle
        else:
            low = middle + 1

    return low
