from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        def choose(start: int) -> None:
            if len(path) == k:
                result.append(path[:])
                return
            remaining = k - len(path)
            last_start = n - remaining + 1
            for value in range(start, last_start + 1):
                path.append(value)
                choose(value + 1)
                path.pop()

        choose(1)
        return result
