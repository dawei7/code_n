


def solve():
    for _ in range(int(input())):
        n,c,q=map(int,input().split())
        for i in range(q):
            l,r=map(int,input().split())
            if l<=c<=r:
                start=c-l
                end=r-start
                c=end
        print(c)


if __name__ == "__main__":
    solve()
