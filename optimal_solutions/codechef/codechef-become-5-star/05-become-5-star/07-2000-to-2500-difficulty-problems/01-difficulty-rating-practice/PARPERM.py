import math


def solve():
    N = 10 ** 5 + 5
    is_prime = [True] * N

    for i in range(2, N):
        if is_prime[i]:
            j = i + i
            while j < N:
                is_prime[j] = False
                j += i

    for i in range(int(input())):
        n, k = map(int,input().split())
        p = [1]
        for i in range(int(math.sqrt(n)), n + 1):
            if is_prime[i] and 2 * i > n:
                p.append(i)

        if k <= len(p):
            print('YES')
            print(' '.join(str(x) for x in p[:k]))

        elif k >= n - len(p):
            print('YES')
            sp = set(p)
            for i in range(1, n + 1):
                if i not in sp:
                    print(i, end=' ')

            for i in range(k + len(p) - n):
                print(p[i], end=' ')

            print()
        else:
            print('NO')


if __name__ == "__main__":
    solve()
