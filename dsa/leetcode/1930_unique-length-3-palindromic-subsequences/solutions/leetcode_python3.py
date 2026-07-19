class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        answer = 0
        for outer in "abcdefghijklmnopqrstuvwxyz":
            first = s.find(outer)
            last = s.rfind(outer)
            if first < last:
                answer += len(set(s[first + 1 : last]))
        return answer
