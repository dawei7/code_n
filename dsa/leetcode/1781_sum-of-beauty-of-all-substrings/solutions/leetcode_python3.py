class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for start in range(len(s)):
            frequencies = [0] * 26
            for end in range(start, len(s)):
                frequencies[ord(s[end]) - ord("a")] += 1
                minimum = min(
                    frequency
                    for frequency in frequencies
                    if frequency > 0
                )
                total += max(frequencies) - minimum
        return total
