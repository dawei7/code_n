# cook your dish here


def solve():
    for i in range(int(input())):
        a,b,c,d = map(int,input().split())
        e=a+10*c
        f=b+10*d
        if e<f:
            print('chef')
        elif(e>f):
            print('chefina')
        else:
            print('draw')


if __name__ == "__main__":
    solve()
