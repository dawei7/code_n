# cook your dish here


def solve():
    t=int(input())
    for _ in range(t):
        n,m,k=map(int,input().split())
        a=set(map(int,input().split()))
        b=set(map(int,input().split()))
        c=set(map(int,input().split()))
        res=(a.intersection(b)).intersection(c)
        print(len(res))


if __name__ == "__main__":
    solve()
