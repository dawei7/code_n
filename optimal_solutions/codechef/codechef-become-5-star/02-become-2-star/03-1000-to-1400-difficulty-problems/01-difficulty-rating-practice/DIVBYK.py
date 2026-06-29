# cook your dish here


def solve():
    for x in range(int(input())):
        d,e= map(int,input().split())
        f= list(map(int,input().split()))
        g= 1
        k= 0
        for i in f:
            g *= i
            if g%e == 0:
                k = 1
                break
        if k ==1:
             print("yes")
        else:
            print("no")


if __name__ == "__main__":
    solve()
