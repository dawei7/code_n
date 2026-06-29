# cook your dish here


def solve():
    t=int(input())
    for i in range(t):
        n,p,s=map(int,input().split())
        l=list(map(int,input().split()))
        if sum(l)==n:
            print(100)
        else:
            if sum(l[:p])==p:
                print(s)
            else:
                print(0)


if __name__ == "__main__":
    solve()
