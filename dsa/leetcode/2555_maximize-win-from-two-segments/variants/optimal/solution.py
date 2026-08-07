class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        best_prefix = [0] * (n + 1)
        answer = 0
        left = 0

        for right, position in enumerate(prizePositions):
            while position - prizePositions[left] > k:
                left += 1

            current = right - left + 1
            answer = max(answer, current + best_prefix[left])
            best_prefix[right + 1] = max(best_prefix[right], current)

        return answer
