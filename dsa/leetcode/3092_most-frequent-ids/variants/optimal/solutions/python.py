from heapq import heappop, heappush


def solve(nums: list[int], freq: list[int]) -> list[int]:
    counts: dict[int, int] = {}
    max_heap: list[tuple[int, int]] = []
    answer: list[int] = []

    for identifier, change in zip(nums, freq):
        current = counts.get(identifier, 0) + change
        counts[identifier] = current
        heappush(max_heap, (-current, identifier))

        while max_heap and -max_heap[0][0] != counts[max_heap[0][1]]:
            heappop(max_heap)

        answer.append(-max_heap[0][0] if max_heap else 0)

    return answer
