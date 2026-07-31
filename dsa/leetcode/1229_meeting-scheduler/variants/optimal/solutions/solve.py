def solve(slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
    slots1.sort()
    slots2.sort()
    first = second = 0

    while first < len(slots1) and second < len(slots2):
        start = max(slots1[first][0], slots2[second][0])
        end = min(slots1[first][1], slots2[second][1])
        if end - start >= duration:
            return [start, start + duration]
        if slots1[first][1] < slots2[second][1]:
            first += 1
        else:
            second += 1
    return []
