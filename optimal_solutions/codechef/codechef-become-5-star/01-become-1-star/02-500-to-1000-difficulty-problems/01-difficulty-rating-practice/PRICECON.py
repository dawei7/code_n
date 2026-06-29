# cook your dish here


def solve():
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        p=list(map(int,input().split()))
        a=0
        for i in range(n):
            if p[i]>k:
                a+=(p[i]-k) 
        print(a)


if __name__ == "__main__":
    solve()
