


def solve():
    for _ in range(int(input())):
        nn=int(input())
        ss=[0]+[int(z) for z in input().split()]
        d1=[0]*(nn+1)
        y=[0]*(nn+1)
        for i in range(1,nn+1):
            y[i]=y[i-1]+ss[i]
        for i in range(1,nn+1):
            for j in range(i-1,0,-1):
                if ss[i]<y[i-1]-y[j]:
                    break
                d1[j]+=1 
            for j in range(i+1,nn+1):
                if(ss[i]<y[j-1]-y[i]):
                    break 
                d1[j]+=1 
        for i in range(1,nn+1):
            print(d1[i],end=' ')
        print()


if __name__ == "__main__":
    solve()
