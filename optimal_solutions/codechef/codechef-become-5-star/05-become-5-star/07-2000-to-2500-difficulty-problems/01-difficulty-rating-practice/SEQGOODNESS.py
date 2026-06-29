from math import comb


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        ans = 0
        MOD = 10**9 + 7
        arr.sort()
        for i in range(n):
            if i>=arr[i]-1:
                l = comb(i,arr[i]-1) % MOD
            else:
                continue
            r = pow(2,n-i-1,MOD)
            ans = (ans + (l * r)) % MOD
        print(ans)


if __name__ == "__main__":
    solve()
