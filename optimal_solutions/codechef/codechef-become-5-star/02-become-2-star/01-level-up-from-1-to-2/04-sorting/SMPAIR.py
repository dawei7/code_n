


def solve():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        print(a[0]+a[1])


if __name__ == "__main__":
    solve()
