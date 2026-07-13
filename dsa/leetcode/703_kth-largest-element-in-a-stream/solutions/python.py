from heapq import heappush, heapreplace


def solve(k: int, nums: list[int], stream: list[int]) -> list[int]:
    heap: list[int] = []

    def offer(value: int) -> None:
        if len(heap) < k:
            heappush(heap, value)
        elif value > heap[0]:
            heapreplace(heap, value)

    for value in nums:
        offer(value)

    answer = []
    for value in stream:
        offer(value)
        answer.append(heap[0])

    return answer
