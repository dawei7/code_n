# cook your dish here


def solve():
    for i in range(int(input())):
        n,x=map(int,input().split())
        m=0
        for i in range(n):
            s,r=map(int,input().split())
            if(s>x):
                pass
            else:
                if(r>m):
                    m=r
        print(m)


if __name__ == "__main__":
    solve()
