


def solve():
    n = int(input())
    c = list(map(int, input().split()))
    t = list(map(int, input().split()))

    at=float('inf')
    tr=float('inf')
    attr=float('inf')

    for i in range(n):
        if t[i]==1:
            tr=min(tr,c[i])
        elif t[i]==2:
            at=min(at,c[i])
        else:
            attr=min(attr,c[i])

    print(min(tr+at, attr))


if __name__ == "__main__":
    solve()
