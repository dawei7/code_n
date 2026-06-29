# cook your dish here


def solve():
    for I in range(int(input())):
        a,b,c=map(int,input().split())
        f=-1
        while(a):
            a//=2
            f+=1
        k=f*b+(f-1)*c
        print(k)


if __name__ == "__main__":
    solve()
