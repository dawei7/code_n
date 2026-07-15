"""Optimal solution for LeetCode 1067: Digit Count in Range."""


def solve(d: int, low: int, high: int) -> int:
    def count_up_to(limit: int) -> int:
        if limit <= 0:
            return 0

        total = 0
        place = 1
        while place <= limit:
            lower = limit % place
            current = (limit // place) % 10
            higher = limit // (place * 10)

            if d != 0:
                total += higher * place
                if current > d:
                    total += place
                elif current == d:
                    total += lower + 1
            elif higher > 0:
                total += (higher - 1) * place
                if current > 0:
                    total += place
                else:
                    total += lower + 1

            place *= 10
        return total

    return count_up_to(high) - count_up_to(low - 1)
