# cook your dish here


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = []
        ind = []
        c1 = []
        bc = b.copy()
        minim = float('inf')
        for i in range(n):
            k = (b[i]+a[0])%n
            if(k<minim):
                minim = k
                ind = []
            if(k == minim):
                ind.append(i)
        for i in ind:
            if(i != 0):
                for j in bc[:i]:
                    bc.append(j) 
                bc = bc[i:]
            for k in range(n):
                c.append((a[k]+bc[k])%n)
            c1.append(c)
            c = []
            bc = b.copy()
        if(len(c1)==1):
            print(*c1[0])
        else:
            m = c1[0]
            for l in c1[1:]:
                f = -1
                for i in range(n):
                    if(l[i]>m[i]):
                        f = 0
                        break
                    elif(l[i]<m[i]):
                        f = 1
                        break
                if(f == 1):
                    m = l
            print(*m)


if __name__ == "__main__":
    solve()
