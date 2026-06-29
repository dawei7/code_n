# cook your dish here


def solve():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        if n&1==1: print(-1)
        else: print(abs(sum(a))//2)


if __name__ == "__main__":
    solve()
