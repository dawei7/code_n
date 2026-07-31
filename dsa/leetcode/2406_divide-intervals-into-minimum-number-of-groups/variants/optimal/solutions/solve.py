from heapq import heappop, heappush


def solve(intervals: list[list[int]]) -> int:
    active_ends: list[int] = []
    maximum_overlap = 0

    for left, right in sorted(intervals):
        while active_ends and active_ends[0] < left:
            heappop(active_ends)
        heappush(active_ends, right)
        maximum_overlap = max(maximum_overlap, len(active_ends))

    return maximum_overlap
