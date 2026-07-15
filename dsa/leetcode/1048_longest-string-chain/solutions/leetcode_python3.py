from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        longest_by_word = {}
        best = 1

        for word in sorted(words, key=len):
            longest = 1
            for index in range(len(word)):
                predecessor = word[:index] + word[index + 1 :]
                longest = max(
                    longest,
                    longest_by_word.get(predecessor, 0) + 1,
                )
            longest_by_word[word] = longest
            best = max(best, longest)

        return best

