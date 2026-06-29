


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        ans = 0

        A=list(map(int,input().split()))
        for j in range(n):
            if A[j] > 0:
                ans += A[j]

        print(ans)


if __name__ == "__main__":
    solve()
