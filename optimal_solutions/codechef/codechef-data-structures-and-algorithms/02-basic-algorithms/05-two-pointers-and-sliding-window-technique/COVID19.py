def solve(test_id):
    n = int(input())
    v = list(map(int, input().split()))
    mn = n
    mx = 0
    l = 0
    for i in range(len(v)):
        if i > 0 and v[i] - v[i - 1] > 2:
            l = i
        if i + 1 == len(v) or v[i + 1] - v[i] > 2:
            cur = i - l + 1
            mn = min(mn, cur)
            mx = max(mx, cur)
    print(mn, mx)

def main():
    tests = int(input())
    for i in range(1, tests + 1):
        solve(i)


if __name__ == "__main__":
    solve()
