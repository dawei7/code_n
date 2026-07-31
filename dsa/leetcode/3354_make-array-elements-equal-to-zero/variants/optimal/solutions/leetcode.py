class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
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
