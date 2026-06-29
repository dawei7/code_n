# cook your dish here


def solve():
    t=int(input())
    for i in range(t):
        a,b=map(int,input().split())
        c= 21 -  (a + b) 
        if c<=10:
            print(c)
        else:
            print("-1")


if __name__ == "__main__":
    solve()
