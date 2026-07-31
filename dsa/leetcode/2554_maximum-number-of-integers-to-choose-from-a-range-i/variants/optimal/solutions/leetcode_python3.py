class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        blocked = set(banned)
        total = 0
        count = 0

        for value in range(1, n + 1):
            if value in blocked:
                continue
            if total + value > maxSum:
                break
            total += value
            count += 1

        return count
