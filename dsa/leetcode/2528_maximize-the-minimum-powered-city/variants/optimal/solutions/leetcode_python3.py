from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        prefix = [0]
        for count in stations:
            prefix.append(prefix[-1] + count)

        power = [
            prefix[min(n, city + r + 1)] - prefix[max(0, city - r)]
            for city in range(n)
        ]

        def feasible(target: int) -> bool:
            difference = [0] * (n + 1)
            active_added = 0
            used = 0

            for city in range(n):
                active_added += difference[city]
                need = target - power[city] - active_added
                if need <= 0:
                    continue

                used += need
                if used > k:
                    return False

                active_added += need
                expires = min(n, city + 2 * r + 1)
                difference[expires] -= need

            return True

        low = min(power)
        high = low + k
        while low < high:
            middle = (low + high + 1) // 2
            if feasible(middle):
                low = middle
            else:
                high = middle - 1
        return low
