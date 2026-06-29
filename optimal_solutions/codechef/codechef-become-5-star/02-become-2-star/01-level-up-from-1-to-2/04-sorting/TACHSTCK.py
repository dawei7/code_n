# cook your dish here


def solve():
    n, d = map(int, input().split())
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    c = 0
    i = 0
    while (i < n - 1):
        if a[i] >= a[i+1] - d:
            c += 1
            i += 1
        i += 1


    print(c)


if __name__ == "__main__":
    solve()
