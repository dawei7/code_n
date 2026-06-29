# cook your dish here


def solve():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        if x >= y:
            print(0)
        else:
            months = y // x
            if y % x == 0:
                months -= 1
            print(months)


if __name__ == "__main__":
    solve()
