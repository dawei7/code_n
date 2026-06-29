


def solve():
    class Solution:
        def C2(self, x: int) -> int:
            return x * (x - 1) // 2

        def process_queries(self, a: list[int], queries: list[int]) -> list[int]:
            n = len(a)
            a.sort()

            counts = [self.C2(n - 1 - i) for i in range(n)]
            for i in range(1, n):
                counts[i] += counts[i - 1]

            result = []
            for k in queries:
                pos = bisect_right(counts, k - 1)
                result.append(a[pos])
            return result


if __name__ == "__main__":
    solve()
