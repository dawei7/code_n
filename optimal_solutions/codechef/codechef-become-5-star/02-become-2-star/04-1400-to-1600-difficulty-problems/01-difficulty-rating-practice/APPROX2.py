# cook your dish here


def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        v = list(map(int, input().split()))
        mini = float('inf')
        for i in range(n-1):
            for j in range(i+1, n):
                mini = min(abs(v[i] + v[j] - k), mini)
        print(mini, end=" ")
        cnt = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if abs(v[i] + v[j] - k) == mini:
                    cnt += 1
        print(cnt)


if __name__ == "__main__":
    solve()
