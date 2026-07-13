class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(left, right):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for center in range(len(s)):
            expand(center, center)
            expand(center, center + 1)
        return count
