class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1, -1, -1]
        total = 0

        for index, char in enumerate(s):
            last[ord(char) - ord("a")] = index
            total += min(last) + 1

        return total
