


def solve():
    for _ in range(int(input())):
        a,b,m = map(int,input().split())
        f = abs(a-b)
        print(min(f,m-f))


if __name__ == "__main__":
    solve()
