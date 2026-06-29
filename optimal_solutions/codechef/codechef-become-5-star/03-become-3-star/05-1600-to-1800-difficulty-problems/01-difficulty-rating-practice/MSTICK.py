


def solve():
    MAX = 10**8 + 1
    MIN = 0

    class SegTree:
        def __init__(self, array, operation, neutral) -> None:
            n = len(array)
            tree = [neutral for _ in range(0, 2 * n)]
            for i in range(0, n):
                tree[n + i] = operation(array[i], neutral)

            for i in reversed(range(1, n)):
                tree[i] = operation(tree[i << 1], tree[i << 1 | 1])

            self._operation = operation
            self._neutral = neutral
            self._n = n
            self._tree = tree

        def query(self, l, r) -> int:
            res = self._neutral
            l += self._n
            r += self._n
            while l < r:
                if l & 1:
                    res = self._operation(res, self._tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = self._operation(res, self._tree[r])

                l >>= 1
                r >>= 1

            return res

    if __name__ == '__main__':
        N = int(input())
        B = list(map(int, input().rstrip().split()))
        Q = int(input())
        max_tree = SegTree(B, max, MIN)
        min_tree = SegTree(B, min, MAX)
        for _ in range(0, Q):
            L, R = tuple(map(int, input().rstrip().split()))
            min_in = min_tree.query(L, R + 1)
            max_in = max_tree.query(L, R + 1)
            max_out = max(max_tree.query(0, L), max_tree.query(R + 1, N))
            ans = float(max((max_in + min_in) / 2, max_out + min_in))
            print(ans)


if __name__ == "__main__":
    solve()
