import heapq


def solve(nums: list[int], k: int) -> int:
    heapq.heapify(nums)
    operations = 0

    while nums[0] < k:
        first = heapq.heappop(nums)
        second = heapq.heappop(nums)
        heapq.heappush(nums, first * 2 + second)
        operations += 1

    return operations
