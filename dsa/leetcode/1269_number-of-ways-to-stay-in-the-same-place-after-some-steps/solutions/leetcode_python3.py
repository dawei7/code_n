class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        modulus = 1_000_000_007
        width = min(arrLen, steps // 2 + 1)
        counts = [0] * width
        counts[0] = 1

        for _ in range(steps):
            next_counts = [0] * width
            for position in range(width):
                total = counts[position]
                if position > 0:
                    total += counts[position - 1]
                if position + 1 < width:
                    total += counts[position + 1]
                next_counts[position] = total % modulus
            counts = next_counts

        return counts[0]
