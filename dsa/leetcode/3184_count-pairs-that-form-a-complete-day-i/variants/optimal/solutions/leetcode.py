class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainder_counts = [0] * 24
        pairs = 0

        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24
            pairs += remainder_counts[complement]
            remainder_counts[remainder] += 1

        return pairs
