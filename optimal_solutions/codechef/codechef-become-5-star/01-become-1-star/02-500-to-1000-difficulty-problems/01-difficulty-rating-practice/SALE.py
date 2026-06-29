# cook your dish here


def solve():
    for i in range(int(input())):
            a,b,c=map(int,input().split())
            print((a+b+c)-min(a,b,c))


if __name__ == "__main__":
    solve()
