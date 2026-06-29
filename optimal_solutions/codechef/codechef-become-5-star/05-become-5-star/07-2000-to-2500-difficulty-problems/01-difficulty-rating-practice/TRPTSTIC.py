


def solve():
    def getVal(i1, j1, i2, j2, a):
        currVal = a[i2][j2]
        if(i1-1>=0):currVal -= a[i1-1][j2]
        if(j1-1>=0):currVal -= a[i2][j1-1]
        if(i1-1>=0 and j1-1>=0):currVal += a[i1-1][j1-1]
        return currVal
    def help(n, a, k):
        for i in range(len(a)):
            for j in range(len(a[0])):
                currVal = getVal(i, j, i, j, a)
                if(currVal!=0):
                    g = getVal(max(0, i-(n//2)), max(0, j-(n//2)), min(len(a)-1, i+(n//2)), min(len(a[0])-1, j+(n//2)), a)
                    if(g>=k):
                        return True
        return False

    for _ in range(int(input())):
        n, m, k = map(int, input().split())
        a = []
        for i in range(n):
            a.append(list(map(int, input().split())))
        for i in range(n):
            for j in range(m):
                if(i-1>=0):a[i][j] += a[i-1][j]
                if(j-1>=0):a[i][j] += a[i][j-1]
                if(i-1>=0 and j-1>=0):a[i][j] -= a[i-1][j-1]
        l = 1
        r = max(n, m)*2+1
        if((r&1)==0):
            r += 1
        temp = []
        for i in range(1, r+1, 2):
            temp.append(i)
        l = 0
        r = len(temp)-1
        f = 0
        while(l<=r):
            m = (l+r)>>1 
            if(help(temp[m], a, k+1)):
                f = 1
                r = m-1
            else:
                l = m+1
        if(f==1):print(temp[l]//2)
        else:print(-1)


if __name__ == "__main__":
    solve()
