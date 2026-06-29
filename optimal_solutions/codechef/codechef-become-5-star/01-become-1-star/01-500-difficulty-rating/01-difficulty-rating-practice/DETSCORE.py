


def solve():
    t=int(input())
    for _ in range(t):
        X,N = map(int,input().split())
        print((X//10)*N)


if __name__ == "__main__":
    solve()
