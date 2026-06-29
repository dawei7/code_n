# cook your dish here


def solve():
    t=int(input())
    for i in range (t):
        n,a,b,c=map(int,input().split())
        d=a+c 
        if n<=d and n<=b:
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    solve()
