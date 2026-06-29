


def solve():
    n=int(input())
    h = list(map(int,input().split()))
    a = h[0]
    c = 1
    for i in range(n):
        if h[i] > a:
            c+=1
            a = h[i]
    print(c)


if __name__ == "__main__":
    solve()
