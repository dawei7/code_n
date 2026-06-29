import sys
from math import *
from collections import *


def solve():
    inp = lambda: sys.stdin.buffer.readline().decode().strip()
    out=sys.stdout.write
    # n=int(inp())
    # arr=list(map(int,inp().split()))
    for _ in range(int(inp())):
        m,n=arr=map(int,inp().split())
        arr=list(map(int,inp().split()))
        arr.sort()
        x=min(m,n)-1
        #a0,a1,....axl-1,(start),,....,(end),am*n-xr,...,am*n-1
        #I need alternately one element from smaller subwindow and one from larger starting with smaller
        #now distribute x into xl and xr such that xl==xr+1 and xl+xr=x if n is odd xl==xr if x is even
        if x%2:
            xl=(x+1)//2
            xr=(x-1)//2
        else:
            xl,xr=x//2,x//2
        s,e=xl,m*n-xr-1
        i,j=s,s+m+n-2
        l,r=-1,-1
        mmin=sys.maxsize
        while j<=e:
            if arr[j]-arr[i]<mmin:
                l,r=i,j
                mmin=arr[j]-arr[i]
            i+=1
            j+=1
        # print(xl,xr,s,e,l,r,mmin)
        ll,rr,i=0,r+1,l
        grid=[[0]*n for _ in range(m)]
        #move right and then down
        if m>=n:
            for j in range(n):
                grid[0][j]=arr[i]
                i+=1
            for j in range(n-1):
                if j%2==0: 
                    grid[1][j]=arr[ll]
                    ll+=1
                else: 
                    grid[1][j]=arr[rr]
                    rr+=1
            for ii in range(1,m):
                grid[ii][n-1]=arr[i]
                i+=1
            temp=deque(arr[ll:l]+arr[i:r+1]+arr[rr:])
            for ii in range(2,m):
                for j in range(n-1):
                    grid[ii][j]=temp.popleft()
        else:
            for ii in range(m):
                grid[ii][0]=arr[i]
                i+=1
            for ii in range(m-1):
                if ii%2==0: 
                    grid[ii][1]=arr[ll]
                    ll+=1
                else: 
                    grid[ii][1]=arr[rr]
                    rr+=1
            for j in range(1,n):
                grid[m-1][j]=arr[i]
                i+=1
            temp=deque(arr[ll:l]+arr[i:r+1]+arr[rr:])
            for ii in range(m-1):
                for j in range(2,n):
                    grid[ii][j]=temp.popleft()
        for g in grid:
            print(*g)


if __name__ == "__main__":
    solve()
