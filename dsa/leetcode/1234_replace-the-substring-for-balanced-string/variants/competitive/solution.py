from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        outside = Counter(s)
        target = len(s) // 4
        if all(outside[character] == target for character in "QWER"):
            return 0

        answer = len(s)
        left = 0
        for right, character in enumerate(s):
            outside[character] -= 1
            while left <= right and all(outside[value] <= target for value in "QWER"):
                answer = min(answer, right - left + 1)
                outside[s[left]] += 1
                left += 1
        return answer
