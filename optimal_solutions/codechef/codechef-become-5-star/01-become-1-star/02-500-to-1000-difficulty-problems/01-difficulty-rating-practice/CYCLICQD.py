# cook your dish here


def solve():
    t=int(input())
    for i in range(t):
        a,b,c,d=map(int,input().split())
        if(a+c==180 and b+d==180):
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    solve()
