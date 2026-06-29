from math import gcd


def solve():
    t = int(input())
    for _ in range(t):
        n,m = list(map(int,input().split()))
        arr = list(map(int,input().split()))
        ans = [arr[0]]
        for i in range(1,n):
            a = m // arr[i]
            b = a * arr[i]
            while gcd(b,arr[i-1])!=arr[i]:
                b -= arr[i]
            ans += [b]
        print(*ans)


if __name__ == "__main__":
    solve()
