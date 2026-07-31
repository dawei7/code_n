from math import lcm

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        reduced = []
        for coin in sorted(coins):
            if not any(coin % kept == 0 for kept in reduced):
                reduced.append(coin)

        upper = min(reduced) * k
        coefficients = {}
        for mask in range(1, 1 << len(reduced)):
            multiple = 1
            parity = 0
            for index, coin in enumerate(reduced):
                if mask >> index & 1:
                    multiple = lcm(multiple, coin)
                    parity ^= 1
            if multiple <= upper:
                coefficients[multiple] = (
                    coefficients.get(multiple, 0)
                    + (1 if parity else -1)
                )

        def count(limit: int) -> int:
            return sum(
                coefficient * (limit // multiple)
                for multiple, coefficient in coefficients.items()
            )

        low, high = 1, upper
        while low < high:
            middle = (low + high) // 2
            if count(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low
