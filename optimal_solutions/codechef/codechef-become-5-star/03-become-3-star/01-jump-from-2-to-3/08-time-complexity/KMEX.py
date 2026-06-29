


def solve():
    for _ in range(int(input())):
        n,m,k=map(int,input().split())
        a=sorted(list(map(int,input().split())))
        c,i=0,0
        while(i<n):
            if i in a:
                i+=1
            elif i==k:
                i+=1
            else:
                i-=1
                break
        if n-a.count(k)>=m and i>=k-1 and m>=k :
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
