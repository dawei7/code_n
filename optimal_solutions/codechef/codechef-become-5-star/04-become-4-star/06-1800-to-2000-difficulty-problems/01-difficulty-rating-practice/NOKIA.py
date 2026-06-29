


def solve():
    def conn_sol(f,l):

        if l-f <=1:

            return 0
        else:
            pos=f + 1 
            global ma
            ma += ((pos-f) + (l-pos))
            conn_sol(pos,l)
    def mi_used(f,l):
        if l-f <=1:
            return 0
        else:
            pos =(f+l) //2
            global mi 
            mi += ((pos-f) + (l-pos))
            mi_used(f,pos)
            mi_used(pos,l)
    for o in range(int(input())):
        n,m = map(int,input().split())
        mi=0
        ma=0
        mi_used(0,n+1)
        conn_sol(0,n+1)
        if mi>m:
            print(-1)
        elif ma > m and mi <=m:
            print(0)
        elif m>=ma:
            print(m-ma)


if __name__ == "__main__":
    solve()
