from typing import List


class Solution:
    def __init__(self):
        self.temporary = [""] * 4
        self.available = 0
        self.position = 0

    def read(self, buf: List[str], n: int) -> int:
        copied = 0
        while copied < n:
            if self.position == self.available:
                self.available = read4(self.temporary)
                self.position = 0
                if self.available == 0:
                    break
            while self.position < self.available and copied < n:
                buf[copied] = self.temporary[self.position]
                copied += 1
                self.position += 1
        return copied
