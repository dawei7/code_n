# cook your dish here


def solve():
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        count=1
        limit=a[0]
        for i in range(1,n):
            if a[i]<=limit:
                count+=1
                limit=a[i]
        print(count)


if __name__ == "__main__":
    solve()
