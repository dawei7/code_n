# cook your dish here


def solve():
    for i in range(int(input())):
        x,a,b,c=map(int,input().split())
        m=min(a,b,c)
        mx=max(a,b,c)
        print((x-1)*m+(a+b+c-m-mx))


if __name__ == "__main__":
    solve()
