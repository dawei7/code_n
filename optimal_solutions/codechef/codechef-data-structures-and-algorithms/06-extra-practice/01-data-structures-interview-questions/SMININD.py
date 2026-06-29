import sys
import bisect

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    q = int(data[1])
    a = list(map(int, data[2:2 + n]))
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]
    results = []
    index = 2 + n
    for _ in range(q):
        i = int(data[index])
        x = int(data[index + 1])
        index += 2
        target = x + prefix[i - 1]
        j = bisect.bisect_left(prefix, target, i, n + 1)
        if j <= n:
            results.append(str(j))
        else:
            results.append('-1')
    sys.stdout.write(' '.join(results))


if __name__ == "__main__":
    solve()
