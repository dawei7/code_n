


def solve():
    MOD = 10**9 + 7
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        even = 0
        for i in arr:
            if i%2==0:
                even += 1
        ans = pow(2,even,MOD)
        print(ans if even!=n else ans-1)


if __name__ == "__main__":
    solve()
