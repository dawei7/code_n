from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n < 2:
            return 0

        prefix = [0]
        for value in stoneValue:
            prefix.append(prefix[-1] + value)

        score = [[0] * n for _ in range(n)]
        best_left = [[0] * n for _ in range(n)]
        best_right = [[0] * n for _ in range(n)]

        for left in range(n - 1, -1, -1):
            best_left[left][left] = stoneValue[left]
            best_right[left][left] = stoneValue[left]
            crossing = left

            for right in range(left + 1, n):
                total = prefix[right + 1] - prefix[left]
                while crossing < right and 2 * (prefix[crossing + 1] - prefix[left]) < total:
                    crossing += 1

                if crossing == right:
                    best = best_left[left][right - 1]
                else:
                    left_sum = prefix[crossing + 1] - prefix[left]
                    left_boundary = crossing if 2 * left_sum == total else crossing - 1
                    best = best_left[left][left_boundary] if left_boundary >= left else 0
                    best = max(best, best_right[crossing + 1][right])

                score[left][right] = best
                best_left[left][right] = max(best_left[left][right - 1], best + total)
                best_right[left][right] = max(best_right[left + 1][right], best + total)

        return score[0][n - 1]
