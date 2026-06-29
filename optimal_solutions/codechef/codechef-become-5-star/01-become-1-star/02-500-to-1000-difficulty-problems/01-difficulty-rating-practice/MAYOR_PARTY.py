# cook your dish here


def solve():
    for _ in range(int(input())):
        a,b,c=map(int,input().split())
        print(max(a+c,b))


if __name__ == "__main__":
    solve()
