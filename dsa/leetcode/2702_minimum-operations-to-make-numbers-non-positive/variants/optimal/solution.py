class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        extra = x - y
        left = 0
        right = (max(nums) + y - 1) // y

        while left < right:
            operations = (left + right) // 2
            required_selections = 0

            for value in nums:
                remaining = value - operations * y
                if remaining > 0:
                    required_selections += (remaining + extra - 1) // extra
                    if required_selections > operations:
                        break

            if required_selections <= operations:
                right = operations
            else:
                left = operations + 1

        return left
