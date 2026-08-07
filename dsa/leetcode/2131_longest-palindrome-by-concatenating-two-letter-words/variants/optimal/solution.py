from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        unmatched = Counter()
        length = 0
        for word in words:
            reverse = word[::-1]
            if unmatched[reverse]:
                unmatched[reverse] -= 1
                length += 4
            else:
                unmatched[word] += 1

        if any(word[0] == word[1] and count for word, count in unmatched.items()):
            length += 2
        return length
