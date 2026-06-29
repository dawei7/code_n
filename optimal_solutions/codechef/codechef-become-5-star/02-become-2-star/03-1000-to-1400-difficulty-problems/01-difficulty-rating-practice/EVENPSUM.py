# cook your dish here


def solve():
    t=int(input())
    for _ in range (t):
        a,b=map(int,input().split())
        evenCountOfA=a//2
        evenCountOfB=b//2
        pairs = (a*b)-(a-evenCountOfA)*evenCountOfB - (b- evenCountOfB)*evenCountOfA
        print(pairs)


if __name__ == "__main__":
    solve()
