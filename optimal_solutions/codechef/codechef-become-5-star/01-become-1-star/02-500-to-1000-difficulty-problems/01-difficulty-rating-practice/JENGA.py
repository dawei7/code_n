# cook your dish here


def solve():
    for _ in range(int(input())):
        n,x = map(int,input().split())
        print("YES") if x%n==0 else print("NO")


if __name__ == "__main__":
    solve()
