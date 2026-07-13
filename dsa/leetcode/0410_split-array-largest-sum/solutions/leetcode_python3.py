class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lower = max(nums)
        upper = sum(nums)

        while lower < upper:
            limit = (lower + upper) // 2
            groups = 1
            current = 0

            for value in nums:
                if current + value > limit:
                    groups += 1
                    current = value
                else:
                    current += value

            if groups <= k:
                upper = limit
            else:
                lower = limit + 1

        return lower
