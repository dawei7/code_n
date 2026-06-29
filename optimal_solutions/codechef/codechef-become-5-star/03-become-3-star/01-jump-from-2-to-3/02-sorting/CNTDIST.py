


def solve():
    n = int(input())

    d = dict()
    for _ in range(n):
        x = int(input())
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    print(2)
    print(len(d))


if __name__ == "__main__":
    solve()
