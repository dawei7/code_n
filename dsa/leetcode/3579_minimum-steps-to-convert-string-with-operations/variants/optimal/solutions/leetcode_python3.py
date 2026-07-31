class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        direct = [[0] * n for _ in range(n)]
        reversed_cost = [[0] * n for _ in range(n)]

        def add_pair(count, mismatches, swaps, source, target):
            if source == target:
                return mismatches, swaps
            x = ord(source) - ord('a')
            y = ord(target) - ord('a')
            mismatches += 1
            if count[x][y] < count[y][x]:
                swaps += 1
            count[x][y] += 1
            return mismatches, swaps

        for left in range(n):
            count = [[0] * 26 for _ in range(26)]
            mismatches = swaps = 0
            for right in range(left, n):
                mismatches, swaps = add_pair(
                    count, mismatches, swaps, word1[right], word2[right]
                )
                direct[left][right] = mismatches - swaps

        for diagonal in range(2 * n - 1):
            count = [[0] * 26 for _ in range(26)]
            mismatches = swaps = 0
            minimum_left = max(0, diagonal - n + 1)
            for left in range(diagonal // 2, minimum_left - 1, -1):
                right = diagonal - left
                if left == right:
                    mismatches, swaps = add_pair(
                        count, mismatches, swaps, word1[left], word2[left]
                    )
                else:
                    mismatches, swaps = add_pair(
                        count, mismatches, swaps, word1[right], word2[left]
                    )
                    mismatches, swaps = add_pair(
                        count, mismatches, swaps, word1[left], word2[right]
                    )
                reversed_cost[left][right] = mismatches - swaps

        best = [n + 1] * (n + 1)
        best[0] = 0
        for right in range(n):
            for left in range(right + 1):
                segment_cost = min(
                    direct[left][right], 1 + reversed_cost[left][right]
                )
                best[right + 1] = min(
                    best[right + 1], best[left] + segment_cost
                )

        return best[n]
