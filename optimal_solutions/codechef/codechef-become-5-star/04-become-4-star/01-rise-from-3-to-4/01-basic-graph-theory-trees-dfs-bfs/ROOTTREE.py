# cook your dish here


def solve():
    for _ in range(int(input())):
        N = int(input())
        noparent = [True]*(N+1)
        z = N
        for i in range(N-1):
            u, v = list(map(int, input().split()))
            if noparent[v]:
                z -= 1
                noparent[v] = False
        print(z-1)


if __name__ == "__main__":
    solve()
