# cook your dish here


def solve():
    for i in range(int(input())):
        a,b,c,d=map(int,input().split())
        a=c//a
        b=d//b
        print(a+b)


if __name__ == "__main__":
    solve()
