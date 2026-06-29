import heapq


def solve():
    def s():
        t=int(input())
        r=[]
        for _ in range(t):
            n,m=map(int,input().split())
            g=[[]for _ in range(n)]
            for _ in range(m):
                a,b=map(int,input().split())
                a-=1
                b-=1
                g[a].append((b,0))
                g[b].append((a,0))
            for i in range(n-1):
                g[i].append((i+1,1))
                g[i+1].append((i,1))
            d=[float('inf')]*n
            d[0]=0
            h=[(0,0)]
            while h:
                c,u=heapq.heappop(h)
                if c>d[u]:continue
                for v,w in g[u]:
                    if c+w<d[v]:
                        d[v]=c+w
                        heapq.heappush(h,(d[v],v))
            r.append(d[-1])
        print('\n'.join(map(str,r)))
    if __name__=="__main__":
        s()


if __name__ == "__main__":
    solve()
