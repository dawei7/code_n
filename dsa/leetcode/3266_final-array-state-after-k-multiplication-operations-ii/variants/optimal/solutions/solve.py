from heapq import heapify, heapreplace


def solve(nums: list[int], k: int, multiplier: int) -> list[int]:
    modulo = 1_000_000_007
    if multiplier == 1:
        return [value % modulo for value in nums]

    heap = [(value, index) for index, value in enumerate(nums)]
    heapify(heap)
    threshold = max(nums)

    while k > 0 and heap[0][0] < threshold:
        value, index = heap[0]
        heapreplace(heap, (value * multiplier, index))
        k -= 1

    heap.sort()
    full_rounds, extra = divmod(k, len(nums))
    answer = [0] * len(nums)
    for position, (value, index) in enumerate(heap):
        exponent = full_rounds + (position < extra)
        answer[index] = value % modulo * pow(multiplier, exponent, modulo) % modulo

    return answer
