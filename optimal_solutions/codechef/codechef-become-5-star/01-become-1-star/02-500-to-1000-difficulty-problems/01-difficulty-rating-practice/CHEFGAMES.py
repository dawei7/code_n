# cook your dish here


def solve():
    t=int(input())
    while t>0:
        a,b,c,d=map(int,input().split())
        if(a==b==c==d==0):
            print("In")
        else:
            print("Out")
        t-=1


if __name__ == "__main__":
    solve()
