import heapq


def solve(nums: list[int], k: int) -> int:
    heapq.heapify(nums)
    for _ in range(k):
        heapq.heapreplace(nums, nums[0] + 1)

    product = 1
    for value in nums:
        product = product * value % 1_000_000_007
    return product
