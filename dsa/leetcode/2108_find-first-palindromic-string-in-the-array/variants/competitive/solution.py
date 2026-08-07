from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            left = 0
            right = len(word) - 1
            while left < right and word[left] == word[right]:
                left += 1
                right -= 1
            if left >= right:
                return word
        return ""
