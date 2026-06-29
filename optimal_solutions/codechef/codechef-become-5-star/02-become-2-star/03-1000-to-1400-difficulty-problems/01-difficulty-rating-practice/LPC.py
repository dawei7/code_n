# cook your dish here


def solve():
    for _ in range(int(input())):
        n,m = map(int, input().split())
        s = input()[:n]
        k = input()[:m]
        ans = float('inf')

        for i in range(n-m+1):
            c = 0
            for j in range(m):
                if s[i + j] != k[j]:
                    a = abs(ord(s[i + j]) - ord(k[j]))
                    if a>5:
                        a = 10-a
                    c += a
            ans = min(ans,c)
        print(ans)


if __name__ == "__main__":
    solve()
