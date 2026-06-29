import sys


def solve():
    input = sys.stdin.readline

    def maxSubArraySum(a, n):
        max_tot = -10**18  # similar to INT_MIN but safe for large values
        m = 0

        for i in range(n):
            m += a[i]
            if max_tot < m:
                max_tot = m

            if m < 0:
                m = 0

        return max_tot


    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        m = int(input())
        b = list(map(int, input().split()))

        p = 0
        for x in b:
            if x > 0:
                p += x

        # Case 1: insert p at beginning
        a.insert(0, p)
        maxx = maxSubArraySum(a, n + 1)

        # Restore
        a.pop(0)

        # Case 2: insert p at end
        a.insert(n, p)
        maxx = max(maxx, maxSubArraySum(a, n + 1))

        print(maxx)


if __name__ == "__main__":
    solve()
