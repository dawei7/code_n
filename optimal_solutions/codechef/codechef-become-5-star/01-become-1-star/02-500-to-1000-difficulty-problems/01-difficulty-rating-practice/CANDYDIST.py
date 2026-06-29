


def solve():
    for i in range(int(input())):
            n,m=map(int,input().split())
            print("YES") if (n/m)%2==0 else print("NO")


if __name__ == "__main__":
    solve()
