from collections import deque


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        minimums = deque()
        maximums = deque()
        left = 0
        answer = 0

        for right, value in enumerate(nums):
            while minimums and nums[minimums[-1]] >= value:
                minimums.pop()
            minimums.append(right)

            while maximums and nums[maximums[-1]] <= value:
                maximums.pop()
            maximums.append(right)

            while (
                nums[maximums[0]] - nums[minimums[0]]
            ) * (right - left + 1) > k:
                if minimums[0] == left:
                    minimums.popleft()
                if maximums[0] == left:
                    maximums.popleft()
                left += 1

            answer += right - left + 1

        return answer
