import heapq


def solve(buildings: list[list[int]]) -> list[list[int]]:
    events = sorted({building[0] for building in buildings} | {building[1] for building in buildings})
    active = [(0, float("inf"))]
    result: list[list[int]] = []
    index = 0
    for x in events:
        while index < len(buildings) and buildings[index][0] == x:
            _, right, height = buildings[index]
            heapq.heappush(active, (-height, right))
            index += 1
        while active[0][1] <= x:
            heapq.heappop(active)
        height = -active[0][0]
        if not result or result[-1][1] != height:
            result.append([x, height])
    return result
