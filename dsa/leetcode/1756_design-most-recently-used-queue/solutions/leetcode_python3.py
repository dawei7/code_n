from collections import deque
from math import isqrt


class MRUQueue:
    def __init__(self, n: int):
        self.block_size = isqrt(n - 1) + 1
        self.blocks = [
            deque(range(start, min(start + self.block_size, n + 1)))
            for start in range(1, n + 1, self.block_size)
        ]

    def fetch(self, k: int) -> int:
        block_index = 0
        while k > len(self.blocks[block_index]):
            k -= len(self.blocks[block_index])
            block_index += 1

        block = self.blocks[block_index]
        block.rotate(-(k - 1))
        value = block.popleft()
        block.rotate(k - 1)

        for index in range(block_index, len(self.blocks) - 1):
            self.blocks[index].append(self.blocks[index + 1].popleft())

        self.blocks[-1].append(value)
        return value
