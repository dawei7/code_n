# cook your dish here


def solve():
    y=int(input())
    for _ in range(y):
        c,v,b=map(int,input().split())
        if c*v <= b*(24*60):print("yes")
        else:print("no")


if __name__ == "__main__":
    solve()
