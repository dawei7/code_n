# cook your di.strip(sh here


def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input())
        print(((n-1)*3)-(((n-1)//2)*3))


if __name__ == "__main__":
    solve()
