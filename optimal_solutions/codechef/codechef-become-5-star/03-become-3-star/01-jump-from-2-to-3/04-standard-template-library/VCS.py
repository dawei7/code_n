# cook your dish here


def solve():
    t=int(input()) 
    for i in range(t): 
        n,m,k=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        first=0
        second=0
        for i in range(1,n+1):
            if i in a and i in b:
                first+=1
            elif i not in a and i not in b:
                second+=1
        print(str(first)+" "+str(second))


if __name__ == "__main__":
    solve()
