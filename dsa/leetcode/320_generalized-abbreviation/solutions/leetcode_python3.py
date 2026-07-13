from typing import List


def _generate_abbreviations(word: str) -> List[str]:
    length = len(word)
    result = []

    for mask in range(1 << length):
        pieces = []
        abbreviated = 0
        for index, letter in enumerate(word):
            if mask & (1 << index):
                abbreviated += 1
                continue
            if abbreviated:
                pieces.append(str(abbreviated))
                abbreviated = 0
            pieces.append(letter)
        if abbreviated:
            pieces.append(str(abbreviated))
        result.append("".join(pieces))

    return result


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        return _generate_abbreviations(word)
