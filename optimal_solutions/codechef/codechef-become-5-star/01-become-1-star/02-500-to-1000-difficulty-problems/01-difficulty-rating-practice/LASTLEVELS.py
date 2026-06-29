# cook your dish here


def solve():
    T=int(input())
    for i in range(T):
        x,y,z=map(int,input().split())
        if(x%3==0):
            b=x//3-1
            tc=x*y+b*z
            print(tc)
        else:
            b=x//3
            tc=x*y+b*z
            print(tc)


if __name__ == "__main__":
    solve()
