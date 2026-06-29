


def solve():
    t = int(input())

    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        happy_days = 0

        for i in range(n):
            if a[i] <= 2 * b[i] and b[i] <= 2 * a[i]:
                happy_days += 1

        print(happy_days)
        t -= 1


if __name__ == "__main__":
    solve()
