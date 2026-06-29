# cook your dish here


def solve():
    n,m,k=map(int,input().split())
    i=1
    c=0
    while(i<=n):
        s=list(map(int,input().split()))
        # print(s)
        i+=1
        if sum(s)-s[k]>=m and s[k]<=10:
            c+=1
    print(c)


if __name__ == "__main__":
    solve()
