# cook your dish here


def solve():
    def h(u):
        u^=u>>16;
        u^=u>>8;
        u^=u>>4;
        u^=u>>2;
        u^=u>>1;
        return not (u&1);
    for bhij in range(int(input())):
        b=int(input())
        l=[]
        i=1
        while i<pow(2,30) and b>0:
            if h(i):
                l.append(i)
                b-=1
            i+=1
        print(*l)


if __name__ == "__main__":
    solve()
