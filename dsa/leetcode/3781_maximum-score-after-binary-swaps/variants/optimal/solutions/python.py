from heapq import heappop, heappush


def solve(nums: list[int], s: str) -> int:
    selected = []
    suffix_capacity = 0

    for index in range(len(nums) - 1, -1, -1):
        if s[index] == "1":
            suffix_capacity += 1
        heappush(selected, nums[index])
        if len(selected) > suffix_capacity:
            heappop(selected)

    return sum(selected)
