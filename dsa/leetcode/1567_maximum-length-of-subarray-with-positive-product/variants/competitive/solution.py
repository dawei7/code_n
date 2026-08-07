from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positive_length = 0
        negative_length = 0
        best = 0

        for value in nums:
            if value == 0:
                positive_length = 0
                negative_length = 0
            elif value > 0:
                positive_length += 1
                negative_length = negative_length + 1 if negative_length else 0
            else:
                positive_length, negative_length = (
                    negative_length + 1 if negative_length else 0,
                    positive_length + 1,
                )

            best = max(best, positive_length)

        return best
