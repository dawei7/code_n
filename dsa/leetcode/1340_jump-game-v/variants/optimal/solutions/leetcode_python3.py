from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        length = len(arr)
        best = [1] * length

        for index in sorted(range(length), key=arr.__getitem__):
            for direction in (-1, 1):
                for distance in range(1, d + 1):
                    destination = index + direction * distance
                    if (
                        destination < 0
                        or destination >= length
                        or arr[destination] >= arr[index]
                    ):
                        break
                    best[index] = max(
                        best[index], 1 + best[destination]
                    )

        return max(best)
