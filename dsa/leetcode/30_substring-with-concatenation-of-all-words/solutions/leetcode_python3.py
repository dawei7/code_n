from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        required = Counter(words)
        result = []

        for offset in range(word_length):
            left = offset
            used = 0
            window = Counter()
            for right in range(offset, len(s) - word_length + 1, word_length):
                word = s[right : right + word_length]
                if word not in required:
                    window.clear()
                    used = 0
                    left = right + word_length
                    continue

                window[word] += 1
                used += 1
                while window[word] > required[word]:
                    left_word = s[left : left + word_length]
                    window[left_word] -= 1
                    used -= 1
                    left += word_length

                if used == len(words):
                    result.append(left)
                    left_word = s[left : left + word_length]
                    window[left_word] -= 1
                    used -= 1
                    left += word_length
        return result
