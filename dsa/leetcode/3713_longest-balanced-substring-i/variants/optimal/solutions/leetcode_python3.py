class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        best = 1

        for left in range(n):
            if n - left <= best:
                break

            counts = [0] * 26
            distinct = 0
            maximum = 0

            for right in range(left, n):
                index = ord(s[right]) - ord("a")
                if counts[index] == 0:
                    distinct += 1
                counts[index] += 1
                maximum = max(maximum, counts[index])

                length = right - left + 1
                if length == distinct * maximum:
                    best = max(best, length)

        return best
