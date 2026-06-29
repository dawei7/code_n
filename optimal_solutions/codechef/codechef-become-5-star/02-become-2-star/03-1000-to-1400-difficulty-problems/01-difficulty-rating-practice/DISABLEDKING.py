# cook your dish here


def solve():
    t=int(input())
    for _ in range(t):
        n=int(input())
        if n&1:
            print(n-1)
        else:
            print(n)


if __name__ == "__main__":
    solve()
