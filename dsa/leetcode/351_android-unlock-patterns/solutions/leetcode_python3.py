from functools import cache


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0] * 10 for _ in range(10)]
        for first, second, middle in (
            (1, 3, 2), (1, 7, 4), (3, 9, 6), (7, 9, 8),
            (1, 9, 5), (3, 7, 5), (2, 8, 5), (4, 6, 5),
        ):
            skip[first][second] = middle
            skip[second][first] = middle

        @cache
        def count(current: int, visited: int, remaining: int) -> int:
            if remaining == 0:
                return 1

            total = 0
            for destination in range(1, 10):
                bit = 1 << destination
                middle = skip[current][destination]
                if not visited & bit and (middle == 0 or visited & (1 << middle)):
                    total += count(destination, visited | bit, remaining - 1)
            return total

        answer = 0
        for length in range(m, n + 1):
            remaining = length - 1
            answer += 4 * count(1, 1 << 1, remaining)
            answer += 4 * count(2, 1 << 2, remaining)
            answer += count(5, 1 << 5, remaining)
        return answer
