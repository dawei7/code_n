class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        even_count = sum(value % 2 == 0 for value in nums)
        odd_count = len(nums) - even_count

        if abs(even_count - odd_count) > 1:
            return -1

        def cost(start_with_even: bool) -> int:
            target = 0 if start_with_even else 1
            swaps = 0

            for index, value in enumerate(nums):
                if value % 2 == 0:
                    swaps += abs(index - target)
                    target += 2

            return swaps

        if even_count > odd_count:
            return cost(True)
        if odd_count > even_count:
            return cost(False)
        return min(cost(True), cost(False))
