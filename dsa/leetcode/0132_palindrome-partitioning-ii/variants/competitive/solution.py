class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)
        palindrome = [[False] * size for _ in range(size)]
        cuts = [0] * size
        for end in range(size):
            cuts[end] = end
            for start in range(end + 1):
                if s[start] == s[end] and (end - start < 2 or palindrome[start + 1][end - 1]):
                    palindrome[start][end] = True
                    cuts[end] = 0 if start == 0 else min(cuts[end], cuts[start - 1] + 1)
        return cuts[-1]
