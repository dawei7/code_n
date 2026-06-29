


def solve():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        x1, y1 = list(map(int, input().split()))
        x2, y2 = list(map(int, input().split()))
        x1, y1, x2, y2 = list(map(lambda val: val - 1, [x1, y1, x2, y2]))

        if (x1 + y1) % 2 != (x2 + y2) % 2:
            for i in range(n):
                for j in range(m):
                    if (i + j) % 2 == (x1 + y1) % 2:
                        print(1, end=" ")
                    else:
                        print(2, end=" ")
                print()
        else:
            def near(x, y, tx, ty):
                return abs(x - tx) + abs(y - ty) == 1

            def near_12(x, y):
                return near(x, y, x1, y1) or near(x, y, x2, y2)

            def same(x, y, tx, ty):
                return x == tx and y == ty

            for i in range(n):
                for j in range(m):
                    if near_12(i, j):
                        print(4, end=" ")
                    elif same(i, j, x2, y2) or (i + j) % 2 != (x1 + y1) % 2:
                        print(2, end=" ")
                    else:
                        print(1, end=" ")
                print()


if __name__ == "__main__":
    solve()
