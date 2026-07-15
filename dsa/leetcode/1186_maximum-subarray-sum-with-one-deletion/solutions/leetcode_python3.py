from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        kept = arr[0]
        deleted = float("-inf")
        answer = arr[0]

        for value in arr[1:]:
            previous_kept = kept
            kept = max(value, kept + value)
            deleted = max(previous_kept, deleted + value)
            answer = max(answer, kept, deleted)

        return answer
