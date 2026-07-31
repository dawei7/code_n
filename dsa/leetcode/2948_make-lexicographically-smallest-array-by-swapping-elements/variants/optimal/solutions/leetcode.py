from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        ordered = sorted((value, index) for index, value in enumerate(nums))
        answer = [0] * len(nums)
        start = 0

        while start < len(ordered):
            end = start + 1
            while end < len(ordered) and ordered[end][0] - ordered[end - 1][0] <= limit:
                end += 1

            indices = sorted(index for _, index in ordered[start:end])
            for index, (value, _) in zip(indices, ordered[start:end]):
                answer[index] = value

            start = end

        return answer
