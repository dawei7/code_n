class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right, char in enumerate(s):
            if char == "1":
                ones += 1

            while ones > k:
                if s[left] == "1":
                    ones -= 1
                left += 1

            if ones == k:
                while left < right and s[left] == "0":
                    left += 1
                candidate = s[left : right + 1]
                if not best or (len(candidate), candidate) < (len(best), best):
                    best = candidate

        return best
