


def solve():
    for _ in range(int(input())):
        amin,bmin,cmin,tmin,a,b,c=map(int,input().split())
        if a>=amin and b>=bmin and c>=cmin:
            if (a+b+c)>=tmin:
                print("yes")
            else:
                print("no")
        else:
            print('no')


if __name__ == "__main__":
    solve()
