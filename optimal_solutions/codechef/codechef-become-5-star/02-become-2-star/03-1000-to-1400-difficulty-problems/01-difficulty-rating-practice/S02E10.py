# cook your dish here
# cook your dish here


def solve():
    for _ in range(int(input())):
        n,x,k=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        c=0
        for i in range(n):
                if abs(a[i]-b[i])<=k:
                    c+=1
        if c>=x:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
