# cook your dish here


def solve():
    t=int(input())
    for t in range(t):
        a,b,c,d=map(int,input().split())
        print(max((a+c),(a+d),(b+c),(b+d)))


if __name__ == "__main__":
    solve()
