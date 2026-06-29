import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    q = int(next(it))

    def v2(x):
        cnt = 0
        while x % 2 == 0:
            cnt += 1
            x //= 2
        return cnt
    arr = [v2(int(next(it))) for _ in range(n)]
    diff = [0] * (n + 1)
    for _ in range(q):
        l = int(next(it))
        r = int(next(it))
        x = int(next(it))
        p = v2(x)
        diff[l - 1] += p
        if r < n:
            diff[r] -= p
    max_power = 0
    current = 0
    for i in range(n):
        current += diff[i]
        arr[i] += current
        if arr[i] > max_power:
            max_power = arr[i]
    sys.stdout.write(str(max_power))


if __name__ == "__main__":
    solve()
