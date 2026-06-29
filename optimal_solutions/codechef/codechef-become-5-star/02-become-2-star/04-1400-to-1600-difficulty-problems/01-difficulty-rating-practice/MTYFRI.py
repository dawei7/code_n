# cook your dish here


def solve():
    for _ in range(int(input())):
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        m,t=[],[]
        for i in range(n):
            if(i%2==0):
                m.append(l[i])
            else:
                t.append(l[i])
        i=0
        while(i<k):
            a=max(m)
            b=min(t)
            m.remove(a)
            t.append(a)
            t.remove(b)
            m.append(b)
            i+=1
        if(sum(m)<sum(t)):
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    solve()
