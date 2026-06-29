


def solve():
    for _ in range(int(input())):
        n,k = map(int,input().split())
        if (n//k)%k: print("YES")
        else: print("NO")


if __name__ == "__main__":
    solve()
