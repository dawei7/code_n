


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        a.sort()

        final = ' '
        element = ''
        for i in range(n):
            if i == n - 1:
                final = ''
                element += str(a[i]) + final
            else:
                element += str(a[i]) + final

        print(element)


if __name__ == "__main__":
    solve()
