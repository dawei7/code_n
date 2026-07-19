from typing import List


class Solution:
    def getModifiedArray(
        self, length: int, updates: List[List[int]]
    ) -> List[int]:
        difference = [0] * length

        for start, end, increment in updates:
            difference[start] += increment
            if end + 1 < length:
                difference[end + 1] -= increment

        running = 0
        for index in range(length):
            running += difference[index]
            difference[index] = running
        return difference

