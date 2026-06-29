


def solve():
    MAXN = 100001
    spf = [0] * (MAXN + 1)
    V = []

    def Sieve():
        spf[1] = 1
        for i in range(2, MAXN):
            spf[i] = i

        for i in range(2, int(MAXN ** 0.5) + 1):
            if spf[i] == i:
                for j in range(2 * i, MAXN, i):
                    if spf[j] == j:
                        spf[j] = i

    def getFactorization(x):
        ret = []
        while x != 1:
            ret.append(spf[x])
            x = x // spf[x]
        return ret

    n = int(input())
    Sieve()
    V = getFactorization(n)
    for i in range(len(V)):
        print(V[i])


if __name__ == "__main__":
    solve()
