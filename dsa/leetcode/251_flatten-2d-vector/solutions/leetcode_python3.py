from typing import List


class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0
        self.column = 0

    def _advance(self) -> None:
        while self.row < len(self.vec) and self.column == len(self.vec[self.row]):
            self.row += 1
            self.column = 0

    def next(self) -> int:
        self._advance()
        value = self.vec[self.row][self.column]
        self.column += 1
        return value

    def hasNext(self) -> bool:
        self._advance()
        return self.row < len(self.vec)
