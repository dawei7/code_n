import heapq


def solve(apples: list[int], days: list[int]) -> int:
    batches: list[tuple[int, int]] = []
    eaten = 0
    day = 0

    while day < len(apples) or batches:
        if day < len(apples) and apples[day] > 0:
            heapq.heappush(batches, (day + days[day], apples[day]))

        while batches and batches[0][0] <= day:
            heapq.heappop(batches)

        if batches:
            expiration, count = heapq.heappop(batches)
            eaten += 1
            if count > 1:
                heapq.heappush(batches, (expiration, count - 1))

        day += 1

    return eaten
