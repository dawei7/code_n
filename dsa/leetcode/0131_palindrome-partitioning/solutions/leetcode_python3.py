from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        size = len(s)
        palindrome = [[False] * size for _ in range(size)]
        for right in range(size):
            for left in range(right, -1, -1):
                palindrome[left][right] = s[left] == s[right] and (
                    right - left < 2 or palindrome[left + 1][right - 1]
                )

        result = []
        path = []

        def search(start):
            if start == size:
                result.append(path.copy())
                return
            for end in range(start, size):
                if palindrome[start][end]:
                    path.append(s[start:end + 1])
                    search(end + 1)
                    path.pop()

        search(0)
        return result
