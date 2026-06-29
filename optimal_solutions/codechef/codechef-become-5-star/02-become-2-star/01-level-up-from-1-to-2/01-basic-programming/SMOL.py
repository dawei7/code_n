# cook your dish here


def solve():
    t=int(input())
    for i in range (t):
        n,k=map(int,input().split())
        if n>=k and k!=0:
            print(n%k)
        else:
            print(n)


if __name__ == "__main__":
    solve()
