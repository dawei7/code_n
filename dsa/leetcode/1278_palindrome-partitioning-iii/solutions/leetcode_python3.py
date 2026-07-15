class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        length = len(s)
        cost = [[0] * length for _ in range(length)]
        for span in range(2, length + 1):
            for left in range(length - span + 1):
                right = left + span - 1
                inner = cost[left + 1][right - 1] if span > 2 else 0
                cost[left][right] = inner + (s[left] != s[right])

        previous = [float("inf")] * (length + 1)
        previous[0] = 0
        for parts in range(1, k + 1):
            current = [float("inf")] * (length + 1)
            for end in range(parts, length + 1):
                current[end] = min(
                    previous[start] + cost[start][end - 1]
                    for start in range(parts - 1, end)
                )
            previous = current
        return previous[length]
