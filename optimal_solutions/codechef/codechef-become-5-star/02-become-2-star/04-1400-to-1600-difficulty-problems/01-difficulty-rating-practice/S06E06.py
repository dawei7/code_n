


def solve():
    t = int(input())
    for tc in range(t):
        N, K = input().split()
        K = int(K)
        num = [int(_) for _ in N]
        for i in range(K):
            n = min(num)
            if n != 9:
                num[num.index(n)] = n+1
            else:
                break
        ans = 1
        for i in num:
            ans *= i
        print(ans)


if __name__ == "__main__":
    solve()
