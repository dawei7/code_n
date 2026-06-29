# cook your dish here


def solve():
    for _ in range(int(input())):
        x,y=map(int,input().split())
        if x==y:
            print(x*2-1)
        else:
            k=x-y
            d=y*2+k
            print(d)


if __name__ == "__main__":
    solve()
