


def solve():
    T = int(input())

    for _ in range(T):
        X, Y, Z = map(int, input().split())
        c = 0

        if X > 0:
            c += 1
        if Y > 0:
            c += 1
        if Z > 0:
            c += 1

        r = [X-1, Y-1, Z-1]
        r.sort()

        if r[0] >= 2:
            c += 3
        elif r[0] == 1 and r[2] >= 2:
            c += 2
        elif r[1] >= 1:
            c += 1

        print(c)


if __name__ == "__main__":
    solve()
