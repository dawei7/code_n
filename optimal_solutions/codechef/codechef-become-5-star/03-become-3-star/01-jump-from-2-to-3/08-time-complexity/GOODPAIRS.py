


def solve():
    for _ in range(int(input())):
        n=int(input())
        a=[int(x) for x in input().split()]
        b=[int(x) for x in input().split()]
        freq={}
        res=0
        for i in range(n-1,-1,-1):
            if (b[i],a[i]) in freq:
                res+=freq[(b[i],a[i])]
            if (a[i],b[i]) in freq:
                freq[(a[i],b[i])]+=1
            else:
                freq[(a[i],b[i])]=1
        print(res)


if __name__ == "__main__":
    solve()
