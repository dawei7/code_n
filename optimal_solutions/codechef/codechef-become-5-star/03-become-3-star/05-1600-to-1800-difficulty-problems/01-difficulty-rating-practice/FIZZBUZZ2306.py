


def solve():
    t = int(input())
    for _ in range(t):
        n,m = list(map(int,input().split()))
        x,y = list(map(int,input().split()))
        down = (n-x) * m
        up = (x-1) * m
        left = (y-1) * n
        right = (m-y) * n
        print(max(up,down,left,right))


if __name__ == "__main__":
    solve()
