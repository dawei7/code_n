from heapq import heapify, heappop, heappush


def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    size = 1 << (n - 1).bit_length()
    minimum = [10**30] * (2 * size)
    maximum = [-1] * (2 * size)
    for index, value in enumerate(nums):
        minimum[size + index] = value
        maximum[size + index] = value
    for index in range(size - 1, 0, -1):
        minimum[index] = min(minimum[2 * index], minimum[2 * index + 1])
        maximum[index] = max(maximum[2 * index], maximum[2 * index + 1])

    def subarray_value(left: int, right: int) -> int:
        left += size
        right += size + 1
        low = 10**30
        high = -1
        while left < right:
            if left & 1:
                low = min(low, minimum[left])
                high = max(high, maximum[left])
                left += 1
            if right & 1:
                right -= 1
                low = min(low, minimum[right])
                high = max(high, maximum[right])
            left //= 2
            right //= 2
        return high - low

    suffix_low = [0] * n
    suffix_high = [0] * n
    suffix_low[-1] = suffix_high[-1] = nums[-1]
    for index in range(n - 2, -1, -1):
        suffix_low[index] = min(nums[index], suffix_low[index + 1])
        suffix_high[index] = max(nums[index], suffix_high[index + 1])

    heap = [
        (-(suffix_high[left] - suffix_low[left]), left, n - 1)
        for left in range(n)
    ]
    heapify(heap)
    answer = 0

    for _ in range(k):
        negative_value, left, right = heappop(heap)
        answer -= negative_value
        if right > left:
            right -= 1
            heappush(heap, (-subarray_value(left, right), left, right))

    return answer
