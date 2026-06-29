


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = []
        val = 1
        lim = 0
        c = 0
        while n:
            n -= 1
            ans += [val]
            c += 1
            if c==pow(2,lim):
                c = 0
                lim += 1
                val += 1
        print(ans[-1])
        print(*ans)


if __name__ == "__main__":
    solve()
