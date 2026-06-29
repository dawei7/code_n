# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        x = set()
        y = set()
        for i in range(n):
            x_i, y_i = map(int, input().split())
            x.add(x_i)
            y.add(y_i)

        print(len(x) + len(y))


if __name__ == "__main__":
    solve()
