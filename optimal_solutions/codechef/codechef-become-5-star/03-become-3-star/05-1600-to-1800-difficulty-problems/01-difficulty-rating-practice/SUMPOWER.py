


def solve():
    for _ in range(int(input())):
        d=[]
        n,k=list(map(int,input().split()))
        s=input()

        pre=None
        for i in s:
            d.append(int(pre!=i))
            pre=i
        #print(d)

        c=sum(d[:k])

        r=0 

        d1,d2=d[:-k],d[k:]
        #print(d1)
        #print(d2)
        for i in range(n-k):
            c+=d2[i]-d1[i]
            r+=c 
        print(r)


if __name__ == "__main__":
    solve()
