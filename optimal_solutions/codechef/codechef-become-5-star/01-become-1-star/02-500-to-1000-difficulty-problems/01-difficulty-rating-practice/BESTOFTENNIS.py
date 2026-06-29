# cook your dish here


def solve():
    for _ in range(int(input())):
        X,Y = map(int,input().split())
        a = max(X,Y)
        print((2*a)-1)


if __name__ == "__main__":
    solve()
