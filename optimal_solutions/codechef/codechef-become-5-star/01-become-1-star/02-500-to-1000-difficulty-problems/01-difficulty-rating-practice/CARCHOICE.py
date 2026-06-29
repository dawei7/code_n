# cook your dish here


def solve():
    for t in range(int(input())):
        a,b,c,d=map(int,input().split())
        if(a/c > b/d):
            print('-1')
        elif(a/c<b/d):
            print('1')
        else:
            print('0')


if __name__ == "__main__":
    solve()
