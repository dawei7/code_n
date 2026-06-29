


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j] * arr[j]:
                res += 1

    print(res)


if __name__ == "__main__":
    solve()
