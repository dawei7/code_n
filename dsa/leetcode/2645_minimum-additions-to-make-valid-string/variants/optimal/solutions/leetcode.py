class Solution:
    def addMinimum(self, word: str) -> int:
        groups = 1

        for previous, current in zip(word, word[1:]):
            if current <= previous:
                groups += 1

        return 3 * groups - len(word)
