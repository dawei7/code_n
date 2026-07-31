from heapq import heapify, heapreplace


def solve(nums: list[int]) -> int:
    n = len(nums) // 3

    left_heap = [-value for value in nums[:n]]
    heapify(left_heap)
    left_sum = sum(nums[:n])
    left = [0] * (2 * n)
    left[n - 1] = left_sum

    for index in range(n, 2 * n):
        value = nums[index]
        if value < -left_heap[0]:
            removed = -heapreplace(left_heap, -value)
            left_sum += value - removed
        left[index] = left_sum

    right_heap = nums[2 * n :]
    heapify(right_heap)
    right_sum = sum(right_heap)
    answer = left[2 * n - 1] - right_sum

    for index in range(2 * n - 1, n - 1, -1):
        value = nums[index]
        if value > right_heap[0]:
            removed = heapreplace(right_heap, value)
            right_sum += value - removed
        answer = min(answer, left[index - 1] - right_sum)

    return answer
