


def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()

        sum_val = sum(a[k:n-k])
        average = sum_val / (n - 2 * k)

        print(f"{average:.6f}")


if __name__ == "__main__":
    solve()
