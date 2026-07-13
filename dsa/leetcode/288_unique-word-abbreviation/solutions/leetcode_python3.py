from typing import List


class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.words = {}
        for word in dictionary:
            abbreviation = self._abbreviate(word)
            if abbreviation not in self.words:
                self.words[abbreviation] = word
            elif self.words[abbreviation] != word:
                self.words[abbreviation] = None

    def _abbreviate(self, word: str) -> str:
        return word if len(word) <= 2 else f"{word[0]}{len(word) - 2}{word[-1]}"

    def isUnique(self, word: str) -> bool:
        abbreviation = self._abbreviate(word)
        return abbreviation not in self.words or self.words[abbreviation] == word
