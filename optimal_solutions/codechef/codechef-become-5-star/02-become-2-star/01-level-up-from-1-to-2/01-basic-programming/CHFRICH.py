# cook your dish here


def solve():
    t = int(input())
    for i in range(t):
        a,b,x = map(int,input().split())

        print((b-a)//x)


if __name__ == "__main__":
    solve()
