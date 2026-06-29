


def solve():
    for _ in range(int(input())):
        a=list(map(int,input().split()))
        l=len(a)
        p=[]
        c=a.count(l-1)
        for i in range(l):
            if(a[i]!=(l-1)):
                p.append(a[i])
        if(c>1):
            for k in range(c-1):
               p.append(l-1)
        print(max(p))


if __name__ == "__main__":
    solve()
