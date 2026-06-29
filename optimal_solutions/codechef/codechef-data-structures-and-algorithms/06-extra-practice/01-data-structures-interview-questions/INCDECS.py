import sys
import bisect

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    res = []

    def compute_lis(arr):
        n = len(arr)
        lis = [0] * n
        dp = []
        for i, x in enumerate(arr):
            pos = bisect.bisect_left(dp, x)
            if pos == len(dp):
                dp.append(x)
            else:
                dp[pos] = x
            lis[i] = pos + 1
        return lis
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        if n == 0:
            res.append('0')
            continue
        lis_left = compute_lis(arr)
        rev_arr = arr[::-1]
        lis_rev = compute_lis(rev_arr)
        lds = [0] * n
        for i in range(n):
            lds[i] = lis_rev[n - 1 - i]
        best = 0
        for i in range(n):
            best = max(best, lis_left[i] + lds[i] - 1)
        res.append(str(best))
    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    solve()
