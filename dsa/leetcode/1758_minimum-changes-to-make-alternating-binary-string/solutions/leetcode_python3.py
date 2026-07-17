class Solution:
    def minOperations(self, s: str) -> int:
        starts_with_zero = sum(
            character != str(index % 2)
            for index, character in enumerate(s)
        )
        return min(starts_with_zero, len(s) - starts_with_zero)
