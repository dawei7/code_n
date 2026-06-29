# cook your dish here


def solve():
    t=int(input())
    for i in range(t):
        x,a,b=map(int,input().split())
        b*=2
        if(x<=(a+b)):
            print("Qualify")
        else:
            print("NotQualify")


if __name__ == "__main__":
    solve()
