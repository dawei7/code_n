


def solve():
    def is_total_coins(h):
        return (h * (h + 1)) // 2

    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = 0
        lo, hi = 1, n
        while lo <= hi:
            mid = (hi + lo) // 2
            if is_total_coins(mid) <= n:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        print(ans)


if __name__ == "__main__":
    solve()
