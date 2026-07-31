from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            used_days = 1
            load = 0
            for weight in weights:
                if load + weight > capacity:
                    used_days += 1
                    load = 0
                load += weight
            return used_days <= days

        low = max(weights)
        high = sum(weights)
        while low < high:
            middle = (low + high) // 2
            if can_ship(middle):
                high = middle
            else:
                low = middle + 1
        return low
