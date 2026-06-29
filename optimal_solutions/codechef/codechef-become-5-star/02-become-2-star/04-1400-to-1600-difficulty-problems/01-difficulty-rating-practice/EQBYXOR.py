


def solve():
    for _ in range(int(input())):
        a,b,n=map(int,input().split())
        x=a^b
        if(a==b):
            print(0)
        elif(x<=n-1):
            print(1)
        elif((n-1)^x<n-1):
            print(2)
        else:
            print(-1)


if __name__ == "__main__":
    solve()
