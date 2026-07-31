class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        best_ending_at = [0] * 26

        for char in s:
            letter = ord(char) - ord("a")
            lower = max(0, letter - k)
            upper = min(25, letter + k)
            previous = max(best_ending_at[lower : upper + 1])
            best_ending_at[letter] = max(
                best_ending_at[letter],
                previous + 1,
            )

        return max(best_ending_at)
