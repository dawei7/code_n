from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pivot = nums.index(k)

        left_counts = {0: 1}
        balance = 0
        for index in range(pivot - 1, -1, -1):
            balance += 1 if nums[index] > k else -1
            left_counts[balance] = left_counts.get(balance, 0) + 1

        answer = 0
        balance = 0
        for index in range(pivot, len(nums)):
            if nums[index] > k:
                balance += 1
            elif nums[index] < k:
                balance -= 1
            answer += left_counts.get(-balance, 0)
            answer += left_counts.get(1 - balance, 0)

        return answer
