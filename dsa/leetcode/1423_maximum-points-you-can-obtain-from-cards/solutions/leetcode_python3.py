from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        remaining_length = len(cardPoints) - k
        if remaining_length == 0:
            return total

        remaining_sum = sum(cardPoints[:remaining_length])
        minimum_remaining = remaining_sum
        for right in range(remaining_length, len(cardPoints)):
            remaining_sum += (
                cardPoints[right] - cardPoints[right - remaining_length]
            )
            minimum_remaining = min(minimum_remaining, remaining_sum)
        return total - minimum_remaining
