# cook your dish here


def solve():
    for i in range(int(input())):
        n,x=map(int,input().split())
        a=int(n/3)
        print(int((n-a)*x))


if __name__ == "__main__":
    solve()
