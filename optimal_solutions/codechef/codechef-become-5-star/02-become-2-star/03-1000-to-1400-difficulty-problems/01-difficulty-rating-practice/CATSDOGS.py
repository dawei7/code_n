


def solve():
    for _ in range(int(input())):
        c,d,l=map(int,input().split())
        if c<=2*d:
            if d*4<=l<=(c*4+d*4) and l%4==0:
                print("yes")
            else:
                print("no")
        elif c>2*d:
            x=c-2*d
            if (x*4+d*4)<=l<=(d*4+c*4) and l%4==0:
                print("yes")
            else:
                print("no")


if __name__ == "__main__":
    solve()
