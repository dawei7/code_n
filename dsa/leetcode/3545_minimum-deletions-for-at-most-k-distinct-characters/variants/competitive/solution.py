class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord("a")] += 1

        frequencies = sorted(count for count in counts if count)
        remove = max(0, len(frequencies) - k)
        return sum(frequencies[:remove])
