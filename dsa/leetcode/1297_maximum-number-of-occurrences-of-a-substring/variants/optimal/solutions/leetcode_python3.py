from collections import Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        del maxSize
        letters = [0] * 26
        distinct = 0
        frequencies = Counter()
        best = 0

        for right, character in enumerate(s):
            index = ord(character) - ord("a")
            if letters[index] == 0:
                distinct += 1
            letters[index] += 1

            if right >= minSize:
                outgoing = ord(s[right - minSize]) - ord("a")
                letters[outgoing] -= 1
                if letters[outgoing] == 0:
                    distinct -= 1

            if right + 1 >= minSize and distinct <= maxLetters:
                window = s[right - minSize + 1 : right + 1]
                frequencies[window] += 1
                best = max(best, frequencies[window])

        return best
