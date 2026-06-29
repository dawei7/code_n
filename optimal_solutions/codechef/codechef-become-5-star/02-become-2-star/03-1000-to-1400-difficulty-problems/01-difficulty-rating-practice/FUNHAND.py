# cook your dish here


def solve():
    for t in range(int(input())):
        n,a,b=map(int,input().split())
        #if abs(a-b)!=1:
        #    print(0)
        #else:
        if abs(a-b)==1:
            if a==1 or b==1 or a==n or b==n:
                print(1)
            #elif a==n or b==n:
            else:
                print(2)
        elif abs(a-b)==2 and (a==b+2 or b==a+2):
            print(1)

        else:
            print(0)


if __name__ == "__main__":
    solve()
