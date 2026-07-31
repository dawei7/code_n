from heapq import heapify, heappop, heappush


def solve(values: list[list[int]]) -> int:
    columns = len(values[0])
    heap = [(row[-1], shop, columns - 1) for shop, row in enumerate(values)]
    heapify(heap)

    spending = 0
    day = 1
    while heap:
        value, shop, column = heappop(heap)
        spending += day * value
        day += 1
        if column > 0:
            heappush(heap, (values[shop][column - 1], shop, column - 1))

    return spending
