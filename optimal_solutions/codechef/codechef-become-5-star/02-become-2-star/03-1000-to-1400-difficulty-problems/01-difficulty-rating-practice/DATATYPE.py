# cook your dish here


def solve():
    for _ in range(int(input())):
        n, x = map(int,input().split())
        print(x%(n+1))


if __name__ == "__main__":
    solve()
