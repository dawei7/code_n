# cook your dish here


def solve():
    for i in range(int(input())):
        a,b=map(int,input().split())
        if(a%2==0 or b%2!=0):
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    solve()
