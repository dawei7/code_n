


def solve():
    class Solution:
        def compute(self, n, x, a, b):
            ans = 0
            for i in range(n):
                if a[i] >= x:
                    ans += b[i]
            return ans


if __name__ == "__main__":
    solve()
