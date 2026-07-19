from typing import List


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        second = 1

        while max(memory1, memory2) >= second:
            if memory1 >= memory2:
                memory1 -= second
            else:
                memory2 -= second
            second += 1

        return [second, memory1, memory2]
