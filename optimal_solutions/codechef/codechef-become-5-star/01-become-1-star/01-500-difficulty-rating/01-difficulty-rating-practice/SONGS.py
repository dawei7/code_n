# cook your dish here


def solve():
    for _ in range(int(input())):
        n,x=map(int, input().split())
        print(n//(3*x))


if __name__ == "__main__":
    solve()
