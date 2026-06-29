import sys
input = sys.stdin.read

def solve():
    data = input().splitlines()
    t = int(data[0])
    index = 1
    for _ in range(t):
        n, k = map(int, data[index].split())
        a = list(map(int, data[index + 1].split()))
        b = list(map(int, data[index + 2].split()))
        v = [(a[i], b[i]) for i in range(n)]
        v.sort(key=lambda x: (x[0] + x[1], -x[0]))
        ans = 0
        cur = 0
        for i in range(n):
            cur += v[i][0] + v[i][1]
            if cur <= k:
                continue
            ans = i
            mn1 = float('inf')
            mn2 = float('inf')
            for j in range(n):
                if v[j][0] + v[j][1] <= v[i][0] + v[i][1]:
                    mn1 = min(mn1, cur - v[j][1])
            if mn1 <= k:
                ans = i + 1
            cur -= v[i][0] + v[i][1]
            for j in range(i, n):
                mn2 = min(mn2, cur + v[j][0])
            cur += v[i][0] + v[i][1]
            if mn2 <= k:
                ans = i + 1
            break
        if cur <= k:
            ans = n
        print(ans)
        index += 3


if __name__ == "__main__":
    solve()
