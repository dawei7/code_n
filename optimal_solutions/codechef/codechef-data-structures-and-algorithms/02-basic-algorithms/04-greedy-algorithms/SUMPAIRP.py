


def solve():
    T = int(input())
    for i in range(1, T + 1):
        N, diff = map(int, input().split())
        arr = list(map(int, input().split()))

        arr.sort()

        sum = 0
        j = N - 1
        while j > 0:
            if (arr[j] - arr[j - 1]) < diff:
                sum += arr[j] + arr[j - 1]
                j -= 2
            else:
                j -= 1

        print(sum)


if __name__ == "__main__":
    solve()
