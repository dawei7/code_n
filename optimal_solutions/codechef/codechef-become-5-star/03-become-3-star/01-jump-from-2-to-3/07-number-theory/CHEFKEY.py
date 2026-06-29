


def solve():
    t = int(input())

    for _ in range(t):
        n, m, c = map(int, input().split())

        factors = list()
        count = 0
        for _ in range(1, c + 1):
            if c % _ == 0:
                factors.append(_)

        for factor in factors:
            other_factor = c // factor

            if factor <= n and other_factor <= m:
                count += 1

        print(count)


if __name__ == "__main__":
    solve()
