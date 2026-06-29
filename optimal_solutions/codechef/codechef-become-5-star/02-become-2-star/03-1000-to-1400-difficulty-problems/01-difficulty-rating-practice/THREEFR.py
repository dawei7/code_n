# cook your dish here


def solve():
    for i in range(int(input())):
        a,b,c=map(int,input().split())
        if( a+b==c or b+c==a or a+c==b):
            print('yes')
        else:
            print('no')


if __name__ == "__main__":
    solve()
