class Solution:
    def minimumPushes(self, word: str) -> int:
        full_levels, remainder = divmod(len(word), 8)
        return 4 * full_levels * (full_levels + 1) + remainder * (full_levels + 1)
