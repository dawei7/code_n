from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        left = set()
        right = Counter(s)
        answer = 0

        for char in s[:-1]:
            left.add(char)
            right[char] -= 1
            if right[char] == 0:
                del right[char]
            answer += len(left) == len(right)

        return answer
