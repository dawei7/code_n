from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.values: List[str | None] = [None] * (n + 1)
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey] = value
        chunk: List[str] = []
        while self.pointer < len(self.values) and self.values[self.pointer] is not None:
            chunk.append(self.values[self.pointer])
            self.pointer += 1
        return chunk
