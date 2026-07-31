from typing import List


class Solution:
    def countStableSubarrays(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(nums)
        prefix = [0] * (n + 1)
        run_start = 0

        for index in range(n):
            if index > 0 and nums[index - 1] > nums[index]:
                run_start = index
            prefix[index + 1] = prefix[index] + index - run_start + 1

        run_ends = [0] * n
        run_end = n - 1
        for index in range(n - 1, -1, -1):
            if index == n - 1 or nums[index] > nums[index + 1]:
                run_end = index
            run_ends[index] = run_end

        answers = []
        for left, right in queries:
            boundary = min(run_ends[left], right)
            first_length = boundary - left + 1
            first_count = first_length * (first_length + 1) // 2
            answers.append(first_count + prefix[right + 1] - prefix[boundary + 1])

        return answers
