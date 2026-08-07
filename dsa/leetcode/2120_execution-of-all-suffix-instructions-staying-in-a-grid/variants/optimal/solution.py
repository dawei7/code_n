from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        moves = {
            "L": (0, -1),
            "R": (0, 1),
            "U": (-1, 0),
            "D": (1, 0),
        }
        answer: List[int] = []

        for start in range(len(s)):
            row, column = startPos
            executed = 0

            for instruction in s[start:]:
                row_change, column_change = moves[instruction]
                row += row_change
                column += column_change
                if not (0 <= row < n and 0 <= column < n):
                    break
                executed += 1

            answer.append(executed)

        return answer
