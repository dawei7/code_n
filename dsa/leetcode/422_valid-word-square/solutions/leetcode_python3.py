from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for row, word in enumerate(words):
            for column, character in enumerate(word):
                if column >= len(words) or row >= len(words[column]):
                    return False
                if words[column][row] != character:
                    return False
        return True
