


def solve():
    for _ in range(int(input())):
        n = int(input())
        dx = dict()
        dy = dict()
        for _ in range(4 * n - 1):
            x, y = map(int, input().split())

            if x in dx:
                dx[x] += 1
            else:
                dx[x] = 1

            if y in dy:
                dy[y] += 1
            else:
                dy[y] = 1

        for key, value in dx.items():
            if value % 2 == 1:
                missing_x = key
                break

        for key, value in dy.items():
            if value % 2 == 1:
                missing_y = key
                break

        print(missing_x, missing_y)


if __name__ == "__main__":
    solve()
