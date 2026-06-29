# cook your dish here


def solve():
    t = int(input())
    for i in range(t):
        a,b,c = map(int,input().split())
        d = b-(a-1)
        print(c*d)


if __name__ == "__main__":
    solve()
