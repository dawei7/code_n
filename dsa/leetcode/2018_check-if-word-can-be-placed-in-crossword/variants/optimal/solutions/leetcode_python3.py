from typing import List


class Solution:
    def placeWordInCrossword(
        self, board: List[List[str]], word: str
    ) -> bool:
        def matches(segment) -> bool:
            if len(segment) != len(word):
                return False
            forward = all(
                cell == " " or cell == letter
                for cell, letter in zip(segment, word)
            )
            backward = all(
                cell == " " or cell == letter
                for cell, letter in zip(segment, reversed(word))
            )
            return forward or backward

        lines = list(board) + list(zip(*board))
        for line in lines:
            segment = []
            for cell in (*line, "#"):
                if cell == "#":
                    if matches(segment):
                        return True
                    segment = []
                else:
                    segment.append(cell)

        return False
