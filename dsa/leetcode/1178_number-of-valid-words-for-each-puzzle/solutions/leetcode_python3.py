from collections import Counter
from typing import List


class Solution:
    def findNumOfValidWords(
        self, words: List[str], puzzles: List[str]
    ) -> List[int]:
        counts = Counter()
        for word in words:
            mask = 0
            for character in set(word):
                mask |= 1 << (ord(character) - ord("a"))
            if mask.bit_count() <= 7:
                counts[mask] += 1

        answers = []
        for puzzle in puzzles:
            required = 1 << (ord(puzzle[0]) - ord("a"))
            optional = 0
            for character in puzzle[1:]:
                optional |= 1 << (ord(character) - ord("a"))

            total = 0
            submask = optional
            while True:
                total += counts[submask | required]
                if submask == 0:
                    break
                submask = (submask - 1) & optional
            answers.append(total)

        return answers
