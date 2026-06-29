


def solve():
    t = int(input())

    while t > 0:
        n = int(input())
        d = list(map(int, input().split()))
        is_non_decreasing = True
        for i in range(1, n):
            if d[i] < d[i - 1]:
                is_non_decreasing = False
                break

        print("Yes" if is_non_decreasing else "No")
        t -= 1


if __name__ == "__main__":
    solve()
