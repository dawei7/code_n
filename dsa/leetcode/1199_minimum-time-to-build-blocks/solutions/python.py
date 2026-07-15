from heapq import heapify, heappop, heappush


def solve(blocks: list[int], split: int) -> int:
    completion_times = blocks.copy()
    heapify(completion_times)

    while len(completion_times) > 1:
        heappop(completion_times)
        larger = heappop(completion_times)
        heappush(completion_times, larger + split)
    return completion_times[0]
