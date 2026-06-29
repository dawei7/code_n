


def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        a.sort()
        diff = a[n - 1] - a[0]
        i = 0
        while(k - 1 + i < n):
            if (a[k - 1 + i] - a[i]) < diff:
                diff = a[k - 1 + i] - a[i]
            i += 1
        print(diff)


if __name__ == "__main__":
    solve()
