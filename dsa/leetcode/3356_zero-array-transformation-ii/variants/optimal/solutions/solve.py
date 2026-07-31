class Solution:
    def minZeroArray(
        self,
        nums: list[int],
        queries: list[list[int]],
    ) -> int:
        difference = [0] * (len(nums) + 1)
        available = 0
        used = 0

        for index, needed in enumerate(nums):
            available += difference[index]
            while available < needed:
                if used == len(queries):
                    return -1

                left, right, value = queries[used]
                used += 1
                if right < index:
                    continue

                start = max(left, index)
                difference[start] += value
                difference[right + 1] -= value
                if start == index:
                    available += value

        return used


def solve(nums: list[int], queries: list[list[int]]) -> int:
    return Solution().minZeroArray(nums, queries)
