


def solve():
    a,b=map(int,input().split())
    c=a-b
    if c%10==9:
        print(c-1)
    else:
        print(c+1)


if __name__ == "__main__":
    solve()
