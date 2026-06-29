


def solve():
    for _ in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        minm=min(a)
        print(minm*(n-1))


if __name__ == "__main__":
    solve()
