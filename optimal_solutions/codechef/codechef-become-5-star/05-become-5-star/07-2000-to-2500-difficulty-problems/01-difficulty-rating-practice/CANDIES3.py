# Uses approach given in editorial <https://discuss.codechef.com/t/candies3-editorial/104926>


def solve():
    def LII():
        return [int(x) for x in input().split()]

    for _ in range(int(input())):
        n, m = LII()
        a = LII()
        c = LII()
        hist = [0] * (m + 1)
        for x in a:
            hist[x] += 1
        for i in reversed(range(m)):
            hist[i] += hist[i + 1]
        print(max(c[p - 1] * sum(hist[k * p] for k in range(1, m // p + 1)) for p in range(1, m + 1)))


if __name__ == "__main__":
    solve()
