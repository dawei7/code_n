


def solve():
    for _ in range(int(input())):
        a,b = map(int,input().split())
        if (a==1 and b==1):
            print(1)
        elif (b==1 and a!=1):
            print(-1)
        else:
             for i in range(1,a+1):
                 if i!=b:
                     print(i,end = " ")
             print(b)


if __name__ == "__main__":
    solve()
