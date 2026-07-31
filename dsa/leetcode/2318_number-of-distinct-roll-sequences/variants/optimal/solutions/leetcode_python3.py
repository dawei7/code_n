from math import gcd


class Solution:
    def distinctSequences(self, n: int) -> int:
        modulus = 1_000_000_007
        if n == 1:
            return 6

        counts = [[0] * 7 for _ in range(7)]
        for previous in range(1, 7):
            for last in range(1, 7):
                if previous != last and gcd(previous, last) == 1:
                    counts[previous][last] = 1

        for _ in range(3, n + 1):
            next_counts = [[0] * 7 for _ in range(7)]
            for previous in range(1, 7):
                for last in range(1, 7):
                    count = counts[previous][last]
                    if count == 0:
                        continue
                    for current in range(1, 7):
                        if (
                            current != previous
                            and current != last
                            and gcd(last, current) == 1
                        ):
                            next_counts[last][current] += count
            counts = next_counts

        return sum(map(sum, counts)) % modulus
