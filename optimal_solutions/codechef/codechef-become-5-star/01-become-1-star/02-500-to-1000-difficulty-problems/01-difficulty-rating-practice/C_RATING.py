# cook your dish here


def solve():
    for _ in range(int(input())):
        x,y = map(int,input().split())
        print((y-x)//8) if (y-x)%8==0 else print((y-x)//8+1)


if __name__ == "__main__":
    solve()
