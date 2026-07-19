from math import isqrt


class Solution:
    def reachNumber(self, target: int) -> int:
        distance = abs(target)
        steps = (isqrt(1 + 8 * distance) - 1) // 2
        total = steps * (steps + 1) // 2

        if total < distance:
            steps += 1
            total += steps

        while (total - distance) % 2:
            steps += 1
            total += steps

        return steps
