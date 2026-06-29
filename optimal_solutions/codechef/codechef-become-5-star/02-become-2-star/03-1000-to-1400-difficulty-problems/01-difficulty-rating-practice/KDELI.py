


def solve():
    t = int(input())

    for _ in range(t):
        n, k, pos = map(int, input().split())
        if pos > n:
            print("0")
            continue

        a = list(map(int, input().split()))
        a.sort(reverse=True)

        total_sum = 0
        while pos <= n:
            total_sum += a[pos - 1]
            pos += k

        print(total_sum)


if __name__ == "__main__":
    solve()
