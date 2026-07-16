class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length = len(nums)
        difference = [0] * (length + 1)
        for left, right in requests:
            difference[left] += 1
            difference[right + 1] -= 1

        coverage = []
        active = 0
        for index in range(length):
            active += difference[index]
            coverage.append(active)

        nums.sort()
        coverage.sort()
        return sum(value * count for value, count in zip(nums, coverage)) % 1_000_000_007
