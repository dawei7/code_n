# cook your dish here


def solve():
    for i in range(int(input())):
        a,b=map(int,input().split())
        s=a*(a-1)//2
        f=a-(2*b)
        if(b<a/2):

            s=s-f*(f-1)//2
        print(s)


if __name__ == "__main__":
    solve()
