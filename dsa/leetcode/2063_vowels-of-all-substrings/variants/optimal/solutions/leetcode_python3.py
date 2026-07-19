class Solution:
    def countVowels(self, word: str) -> int:
        length = len(word)
        return sum(
            (index + 1) * (length - index)
            for index, character in enumerate(word)
            if character in "aeiou"
        )
