import math


def solve():
    t = int(input())
    for _ in range(t):
        m,n = list(map(int,input().split()))
        M = m
        if m==n:
            print("YES")
        elif m<n:
            print("NO")
        else:
            while M and M%2==0:
                M //= 2
            print("YES" if n%M==0 else "NO")


if __name__ == "__main__":
    solve()
