


def solve():
    t=int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        house=0

        minx=m
        miny=n
        maxx=0
        maxy=0

        for i in range(n):
            s=input()
            for j in range(m):
                if(s[j]=="*"):
                    house=house+1

                    if i<miny: 
                        miny=i
                    if i>maxy: 
                        maxy=i
                    if j<minx: 
                        minx=j
                    if j>maxx: 
                        maxx=j

        vdist = maxy-miny+1
        hdist = maxx-minx+1

        if house==0: print(0)
        else: print(1+(max(vdist,hdist))//2)


if __name__ == "__main__":
    solve()
