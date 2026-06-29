


def solve():
    n = int(input())

    v = []
    for _ in range(n):
        x = int(input())
        v.append(x)

    v.sort()

    for num in v:
        print(num)


if __name__ == "__main__":
    solve()
