


def solve():
    MAXN = 10**7
    prime = [True] * (MAXN + 5)
    tot_primes_till = [0] * (MAXN + 5)

    def sieve():
        n = MAXN
        for i in range(2, n + 1):
            tot_primes_till[i] = tot_primes_till[i - 1]

            if not prime[i]:
                continue

            tot_primes_till[i] += 1

            for j in range(2 * i, n + 1, i):
                prime[j] = False

    sieve()

    tests = int(input())

    for _ in range(tests):
        X, Y = map(int, input().split())
        ans = Y - X - (tot_primes_till[Y] - tot_primes_till[X + 1])
        print(ans)


if __name__ == "__main__":
    solve()
