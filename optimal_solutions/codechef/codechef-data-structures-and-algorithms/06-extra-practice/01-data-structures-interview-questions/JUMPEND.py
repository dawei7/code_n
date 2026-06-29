


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        goal = n - 1
        ans = 0
        for i in range(n - 2, -1, -1):
            if i + arr[i] >= goal:
                ans += 1
                goal = i
        if goal == 0:
            print(ans)
        else:
            print(-1)


if __name__ == "__main__":
    solve()
