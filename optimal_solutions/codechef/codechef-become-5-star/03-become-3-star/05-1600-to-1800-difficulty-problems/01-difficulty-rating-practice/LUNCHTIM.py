import sys
from collections import defaultdict

def mod(x, n, M):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return mod(x * x % M, n // 2, M)
    else:
        return x * mod(x * x % M, (n - 1) // 2, M) % M

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        m = list(map(int, sys.stdin.readline().split()))
        c = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if m[j] > m[i]:
                    break
                elif i != j and m[i] == m[j]:
                    c[i] += 1
            for j in range(i - 1, -1, -1):
                if m[j] > m[i]:
                    break
                elif i != j and m[i] == m[j]:
                    c[i] += 1
            sys.stdout.write(str(c[i]) + ' ')
        sys.stdout.write('\n')


if __name__ == "__main__":
    solve()
