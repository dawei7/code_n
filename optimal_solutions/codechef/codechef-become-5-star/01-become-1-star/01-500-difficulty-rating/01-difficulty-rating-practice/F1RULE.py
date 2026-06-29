# cook your dish here


def solve():
    t=int(input())
    for i in range(t):
        x,y=map(int,input().split())
        a=107/100
        if a*x>=y:
            print("YES")
        else:
            print("No")


if __name__ == "__main__":
    solve()
