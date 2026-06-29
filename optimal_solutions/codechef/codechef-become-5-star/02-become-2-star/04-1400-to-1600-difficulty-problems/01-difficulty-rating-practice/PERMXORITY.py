# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        if n == 2:
            print(-1)
        else:
            a = list(range(1, n + 1))
            if n % 2 == 0:
                a.insert(1, n)
                a = a[:-1]
            print(*a)


if __name__ == "__main__":
    solve()
