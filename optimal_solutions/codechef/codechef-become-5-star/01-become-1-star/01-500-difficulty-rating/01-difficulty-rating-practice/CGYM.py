# cook your dish here


def solve():
    t=int(input())
    for i in range(t):
        a,b,c=map(int,input().split())
        if(a+b<=c):
            print('2')
        elif(a<=c):
            print('1')
        else:
            print('0')


if __name__ == "__main__":
    solve()
