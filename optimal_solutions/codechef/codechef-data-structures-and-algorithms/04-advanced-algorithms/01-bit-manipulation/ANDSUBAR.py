def largest_pow(n):
    p = 1
    while p * 2 <= n:
        p *= 2
    return p

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lp = largest_pow(n)
        secLp = lp // 2
        ans1 = n - lp + 1
        ans2 = lp - secLp
        print(max(ans1, ans2))


if __name__ == "__main__":
    solve()
