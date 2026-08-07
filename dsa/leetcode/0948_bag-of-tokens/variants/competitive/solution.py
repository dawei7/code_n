from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ordered = sorted(tokens)
        left = 0
        right = len(ordered) - 1
        score = 0
        best = 0

        while left <= right:
            if power >= ordered[left]:
                power -= ordered[left]
                left += 1
                score += 1
                best = max(best, score)
            elif score > 0 and left < right:
                power += ordered[right]
                right -= 1
                score -= 1
            else:
                break

        return best
