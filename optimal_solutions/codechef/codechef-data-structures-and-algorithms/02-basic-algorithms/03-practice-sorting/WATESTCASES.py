


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        v = input()
        ans = 101
        for i in range(n):
            if v[i] == '0':
                ans = min(ans, s[i])
        print(ans)


if __name__ == "__main__":
    solve()
