from math import isqrt


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 0
        high = min(ranks) * cars * cars

        while low < high:
            time = (low + high) // 2
            repaired = sum(isqrt(time // rank) for rank in ranks)

            if repaired >= cars:
                high = time
            else:
                low = time + 1

        return low
