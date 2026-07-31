class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        answer = 0

        for value in nums:
            if value == 0:
                right = total - left
                if left == right:
                    answer += 2
                elif abs(left - right) == 1:
                    answer += 1
            left += value

        return answer


def solve(nums: list[int]) -> int:
    return Solution().countValidSelections(nums)
