# cook your dish here


def solve():
    for _ in range(int(input())):
        a,b=map(int,input().split())
        z=a-b
        print(min(z,b))


if __name__ == "__main__":
    solve()
